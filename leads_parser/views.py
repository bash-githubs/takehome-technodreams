from rest_framework.response import Response
from rest_framework import status, viewsets
from .tasks import extract_csv_data
from celery.result import AsyncResult
from .serializer import CustomerSerializer
from .validators import is_time_within_range
import base64
from .models import Customer


class LeadsManagementViewSet(viewsets.ViewSet):

    def create(self, request):
        if not is_time_within_range():
            return Response({"message": "user can not upload data at this time"}, status=status.HTTP_400_BAD_REQUEST)
        data = request.FILES.get('file')
        data = base64.b64encode(data.read()).decode('utf-8')
        task = extract_csv_data.delay(data)
        return Response({"message": task.id, "status": task.status}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        task_result = AsyncResult(pk)
        if task_result.status != 'SUCCESS':
            return Response({"message": "task is still processing", "status": task_result.status, "task_id": task_result.id}, status=status.HTTP_200_OK)
        customers = Customer.objects.filter(sheet_id=task_result.result)
        customer_result = CustomerSerializer(customers, many=True)
        return Response({"message": "successful", "data": customer_result.data}, status=status.HTTP_200_OK)
