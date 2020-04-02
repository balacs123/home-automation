from django.db import models
from jsonfield import JSONField


class Devices(models.Model):
    device_id = models.TextField(unique=True)
    device_name = models.TextField(blank=False)
    device_status = models.TextField(blank=False, default="Nil")
    device_operation = JSONField(default={})

