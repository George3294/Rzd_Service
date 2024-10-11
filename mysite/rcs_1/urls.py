from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import InfoIndexView, StationListView, ArduinoCreateView, ArduinoListView, usb_web, StationCreateView, MicrocomputerListView, MicrocomputerCreateView
app_name = 'rcs_1'

routers = DefaultRouter()

urlpatterns = [
    path('', InfoIndexView.as_view(), name='info-index'),
    path("station/", StationListView.as_view(), name="info-list"),
    path("station/create/", StationCreateView.as_view(), name="info-create"),
    path("arduino/create/", ArduinoCreateView.as_view(), name="arduino-create"),
    path("arduino/list/", ArduinoListView.as_view(), name="arduino-list"),
    path("arduino/info/", usb_web, name="info-arduino"),
    path("micro/create/", MicrocomputerCreateView.as_view(), name="micro-create"),
    path("micro/list/", MicrocomputerListView.as_view(), name="micro-list"),
]