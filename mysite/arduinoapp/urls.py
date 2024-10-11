from django.urls import include
from django.urls import path
from .views import (InfoIndexView,
                    InfoIndexRCS,
                    StationCreateView,
                    StationListView,
                    ArduinoCreateView,
                    ArduinoListView,
                    StationViewSet,
                    usb_web)
from rest_framework.routers import DefaultRouter
app_name = 'arduinoapp'

routers = DefaultRouter()
routers.register("station", StationViewSet)
urlpatterns = [
    path('', InfoIndexView.as_view(), name='info-index'),
    path("rcs/", InfoIndexRCS.as_view(), name = "rcs-index"),
    path("api/", include(routers.urls)),
    path("station/", StationListView.as_view(), name="info-list"),
    path("station/create", StationCreateView.as_view(), name="info-create"),
    path("arduino/create", ArduinoCreateView.as_view(), name="arduino-create"),
    path("arduino/list", ArduinoListView.as_view(), name="arduino-list"),
    path("arduino/info",usb_web, name="info-arduino"),
]