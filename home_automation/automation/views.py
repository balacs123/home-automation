from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

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
        obj.device_operation = {"operations": data['device_operation']}
        obj.save()

        serializer = DeviceSerializer(obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeviceUpdate(APIView):
    def put(self, request, device_id):
        data = request.data
        print(data)
        serializer = DevicePostSerializer(data=data)
        if not serializer.is_valid():
            raise AppException(serializer.errors)
        try:
            obj = Devices.objects.get(device_id=device_id)
        except ObjectDoesNotExist:
            return Response("Given device is not available")
        obj.device_id = data['device_id']
        obj.device_name = data['device_name']
        obj.device_operation = {"operations": data['device_operation']}
        obj.save()

        serializer = DeviceSerializer(obj)
        return Response(serializer.data)

    def delete(self, request, device_id):
        try:
            obj = Devices.objects.get(device_id=device_id)
        except ObjectDoesNotExist:
            return Response("Given device is not available")
        obj.delete()
        return Response("Device deleted successfully")


class DeviceStatus(APIView):

    def put(self, request, device_id):
        data = request.data
        try:
            device = Devices.objects.get(device_id=device_id)
        except ObjectDoesNotExist:
            return "Given device is not available"
        print(device.device_operation['operations'])
        operation = device.device_operation
        if data['device_status'] not in operation['operations']:
            return Response("Given status is not available in device operations")
        device.device_status = data['device_status']
        device.save()

        serializer = DeviceSerializer(device)
        return Response(serializer.data)

