import calendar
import csv
import datetime
from argparse import Action
import logging
from csv import DictWriter
from io import TextIOWrapper
from re import split
from timeit import default_timer
from urllib.request import Request
from requests import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.admin import action
from django.http import HttpRequest, HttpResponse, JsonResponse, response
from django.http.multipartparser import MultiPartParser
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView
from rest_framework.utils import json
from rest_framework.viewsets import ModelViewSet
from twisted.protocols.sip import Response
from .common import save_csv_stations
from .forms import StationForm
from .models import Station, Arduino, Sensor_Data
import serial
from .serializer import StationSerializer
import requests
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
# Create your views here.


log = logging.getLogger(__name__)
@extend_schema(description="Station views CRUD")
class StationViewSet(ModelViewSet):
    """"
    Набор представлений для действий над Station
    Полный CRUD для операций над станциями
    """
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]

    filterset_fields = [
        "name",
        "temperature_info",
        "data_created",
    ]
    @extend_schema(
        summary="Get one station ID",
        description="Retrieves **station**, returns 404 if not found",
        responses={
            200: StationSerializer,
            404: OpenApiResponse(description="Empty response, station by id not found")
        }
    )
#    @action(methods=["get"], detail=False)
    def download_csv(self, request: Request):
        response = HttpResponse(content_type='text/csv')
        filename = "info-station.csv"
        response["Content-Disposition"] = f"attachment; filename={filename}"
        queryset = self.filter_queryset(self.get_queryset())
        fields = [
            "name",
            "temperature_info",
            "data_created",
        ]
        queryset = queryset.only(*fields)
        writer = DictWriter(response, fieldnames=fields)
        writer.writeheader()

        for station in queryset:
            writer.writerow({
                field: getattr(station, field)
                for field in fields
            })
            return response
#    @action(
        detail=False,
        methods = ["post"],
        parser_classes=[MultiPartParser]
#    )
    def upload_csv(self, request: Request):
        stations = save_csv_stations(
            request.FILES["file"],
            encoding=request.encoding,
        )
        serializer = self.get_serializer(stations, many=True)
        return Response(serializer.data)


class InfoIndexRCS(View):
    """
    Страница трех РЦС
    """
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "arduinoapp/rcs-index.html")

    def calendar_view(request):
        cal = calendar.monthcalendar(year=2024, month=10)
        context = {
            'calendar': cal,
        }
        return render(request, "arduinoapp/rcs-index.html", context=context)


class InfoSettingsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "arduinoapp/info-settings.html")

class InfoAboutRCS4(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "arduinoapp/info-aboutRCS4.html")

class Saratov_1RCS4(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "arduinoapp/info-Saratov_1RCS4.html")

class InfoIndexView(View):
    """
    Главная страница сайта
    """
    def get(self, request: HttpRequest) -> HttpResponse:
        stations = [
            ('Новая НС', 28),
            ('Аткарск', 30),
            ('Саратов-1', 28),
        ]
        context = {
            "time_running": default_timer(),
            'station': stations,
        }
        log.debug("Станции их индексы: %s", stations)
        log.info("Станции")
        print("Станции", context)
        return render(request, "arduinoapp/info-index.html", context=context)



class StationListView(ListView):
    """
    Список станций и какая-то информация о ней
    """
    template_name = "arduinoapp/info-list.html"
    context_object_name = "station"
    queryset = Station.objects.all()


def station_create(self, request: HttpRequest) -> HttpResponse:
    """
    POST запрос на создание станции
    :param self:
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse("arduinoapp/info-list.html")
            return redirect(url)
    else:
        form = StationForm()
    context = {
        "form": form,
    }
    return render(request, "arduinoapp/info-create.html", context=context)


class StationCreateView(CreateView):
    """
    Создание станции и какая-то информация о ней
    """
    model = Station
    fields = "name", "temperature_info", "documents",
    template_name = 'arduinoapp/info-create.html'
    success_url = reverse_lazy("arduinoapp:info-create")
    
    
class ArduinoCreateView(CreateView):
    """
    Создание Arduino и какая-то информация о ней
    """
    model = Arduino
    fields = "name", "temperature_info", "station"
    template_name = 'arduinoapp/arduino-create.html'
    success_url = reverse_lazy("arduinoapp:arduino-create")
    
    
class ArduinoListView(ListView):
    """
    Список Arduino
    """
    template_name = "arduinoapp/arduino-list.html"
    context_object_name = "arduinos"
    queryset = Arduino.objects.all()


def usb_web(request: HttpRequest) -> HttpResponse:
    """
    Информация с Arduino
    """
    with open("arduino.csv", "r", encoding="utf-8") as file:
        for line in file.read().split("\n"): # Про тестить maxsplit, что бы произвести разделение на несколько строк
            name = line.strip().split(",")
            Sensor_Data.objects.create(name=name)
            data_sensor = [
                ("", line)
            ]
            context = {
                "data_sensor": data_sensor,
            }
            return render(request, "arduinoapp/info-arduino.html", context=context)

class DataSensorListView(ListView):
    """
    Информаця с Arduino для анализа
    и работы с этими данными
    """
    template_name = "arduinoapp/info-arduino.html"
    context_object_name = "Sensor_datas"
    queryset = Sensor_Data.objects.all()



