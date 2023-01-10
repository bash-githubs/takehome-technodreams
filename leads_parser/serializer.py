from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ("file",)
