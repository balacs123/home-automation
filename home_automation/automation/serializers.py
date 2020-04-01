from rest_framework import serializers
from .models import *


class DeviceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    device_id = serializers.CharField()
    device_name = serializers.CharField()
    device_status = serializers.CharField()
    device_operation = serializers.DictField()


class DevicePostSerializer(serializers.Serializer):
    device_id = serializers.CharField()
    device_name = serializers.CharField()
    device_operation = serializers.DictField()