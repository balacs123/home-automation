from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from automation.models import Devices
from automation.serializers import *
from utils.exceptions import AppException


class DeviceList(APIView):
    def get(self, request):
        objs = Devices.objects.all().order_by('id')
        serializer = DeviceSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        obj = Devices()
        serializer = DevicePostSerializer(data=data)
        if not serializer.is_valid():
            raise AppException(serializer.errors)
        obj.device_id = data['device_id']
        obj.device_name = data['device_name']
        obj.device_operation = data['device_operation']
        obj.save()

        serializer = DeviceSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeviceUpdate(APIView):
    def put(self, request, device_id):
        data = request.data
        obj = Devices.objects.get(device_id=device_id)
        serializer = DevicePostSerializer(data=data)
        if not serializer.is_valid():
            raise AppException(serializer.errors)
        obj.device_id = data['device_id']
        obj.device_name = data['device_name']
        obj.device_operation = data['device_operation']
        obj.save()

        serializer = DeviceSerializer(obj, many=True)
        return Response(serializer.data)

    def delete(self, device_id):
        obj = Devices.objects.get(device_id=device_id)
        obj.delete()
        return Response("Device deleted successfully")
