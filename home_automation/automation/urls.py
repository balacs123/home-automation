from django.conf.urls import url

from automation.views import *

urlpatterns = [
    url(r'^list$', DeviceList.as_view()),
    url(r'^(?P<id>[EI].[0-9]*)$', DeviceUpdate.as_view()),
    ]