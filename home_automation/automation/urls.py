from django.conf.urls import url

from automation.views import *

urlpatterns = [
    url(r'^$', DeviceList.as_view()),
    url(r'^(?P<device_id>[a-zA-Z0-9]*)$', DeviceUpdate.as_view()),
    url(r'^status/(?P<device_id>[a-zA-Z0-9]*)$', DeviceStatus.as_view()),
    ]
