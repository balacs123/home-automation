from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError


from automation.models import Devices
from automation.serializers import *
from utils.exceptions import AppException

import logging
logger = logging.getLogger(__name__)


class DeviceList(APIView):
    def get(self, request):
        objs = Devices.objects.all().order_by('id')
        if not objs:
            logger.info("No device available to show")
            return Response("No device available to show")
        serializer = DeviceSerializer(objs, many=True)
        logger.info('Displaying all device info')
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = DevicePostSerializer(data=data)
        if not serializer.is_valid():
            raise AppException(serializer.errors)
        try:
            obj = Devices()
            obj.device_id = data['device_id']
            obj.device_name = data['device_name']
            obj.device_operation = {"operations": data['device_operation']}
            obj.save()
        except IntegrityError:
            logger.info("Device is already available. Please check your device details")
            return Response("Device is already available. Please check your device details")

        logger.info("Added new smart device - {}".format(obj.device_id))
        serializer = DeviceSerializer(obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        objs = Devices.objects.all().order_by('id')
        if not objs:
            logger.info("No Device available to delete")
            return Response("No Device available to delete")
        for obj in objs:
            obj.delete()
        logger.info("All Device deleted succesfully")
        return Response("All Device deleted succesfully")

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
            logger.info("Given device is not available")
            return Response("Given device is not available")
        obj.device_id = data['device_id']
        obj.device_name = data['device_name']
        obj.device_operation = {"operations": data['device_operation']}
        obj.save()

        logger.info("Update device details successfully for device {}".format(device_id))
        serializer = DeviceSerializer(obj)
        return Response(serializer.data)

    def delete(self, request, device_id):
        try:
            obj = Devices.objects.get(device_id=device_id)
        except ObjectDoesNotExist:
            logger.info("Given device is not available")
            return Response("Given device is not available")
        obj.delete()
        logger.info("Device {} deleted successfully".format(device_id))
        return Response("Device {} deleted successfully".format(device_id))


class DeviceStatus(APIView):

    def put(self, request, device_id):
        data = request.data
        try:
            device = Devices.objects.get(device_id=device_id)
        except ObjectDoesNotExist:
            logger.info("Given device is not available")
            return Response("Given device is not available")

        if data['device_status'] not in device.device_operation['operations']:
            logger.info("Given status is not available in device operations")
            return Response("Given status is not available in device operations")
        elif data['device_status'] == device.device_status:
            logger.info("Device {} already in given state".format(device_id))
            return Response("Device already in given state")

        device.device_status = data['device_status']
        device.save()
        logger.info("Device {} status changed to {}".format(device_id, device.device_status))
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

