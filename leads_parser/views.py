import base64

from celery.result import AsyncResult
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Customer
from .serializer import CustomerSerializer
from .tasks import extract_csv_data
from .validators import is_time_within_range


class LeadsManagementViewSet(viewsets.ViewSet):
    def create(self, request):
        if not is_time_within_range():
            return Response(
                {"message": "user can not upload data at this time"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = request.FILES.get("file")
        data = base64.b64encode(data.read()).decode("utf-8")
        task = extract_csv_data.delay(data)
        return Response(
            {
                "task_id": task.id,
                "status": task.status,
                "message": "task is still processing",
            },
            status=status.HTTP_200_OK,
        )

    def retrieve(self, request, pk):
        task_result = AsyncResult(pk)
        if task_result.status != "SUCCESS":
            return Response(
                {
                    "message": "task is still processing",
                    "status": task_result.status,
                    "task_id": task_result.id,
                },
                status=status.HTTP_200_OK,
            )
        customers = Customer.objects.filter(sheet_id=task_result.result)
        customer_result = CustomerSerializer(customers, many=True)
        return Response(
            {"message": "successful", "data": customer_result.data},
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=["get"])
    def csv_headers(self, request):
        excluded_fields = ["id", "created_at", "modified_at", "sheet_id"]
        csv_headers = []
        for f in Customer._meta.get_fields():
            if f.name not in excluded_fields:
                csv_headers.append(f.name)
        return Response(
            {"message": "successful", "data": csv_headers}, status=status.HTTP_200_OK
        )
