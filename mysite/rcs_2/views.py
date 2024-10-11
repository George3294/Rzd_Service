from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from .forms import StationForm
from .models import Station, Arduino, Sensor_Data, Microcomputer


# Create your views here.


class InfoIndexView(View):
    """
    Главная страница сайта
    """
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'rcs_2/info-index.html')

class StationListView(ListView):
    """
    Список станций и какая-то информация о ней
    """
    template_name = 'rcs_2/info-list.html'
    context_object_name ='station'
    queryset = Station.objects.all()

    def station_create(self, request: HttpRequest) -> HttpResponse:
        """
        Создание станции
        :param request:
        :return:
        """
        if request.method == 'POST':
            form = StationForm(request.POST)
            if form.is_valid():
                form.save()
                url = reverse("rcs_2/info-list.html")
                return redirect(url)
        else:
            form = StationForm()
        context = {
            'form': form
        }
        return render(request, 'rcs_2/info-create.html', context=context)

class StationCreateView(CreateView):
    """
    Создание станции и какая-то информация о ней
    """
    model = Station
    fields = "name", "temperature_info", "documents",
    template_name = 'rcs_2/info-create.html'
    success_url = reverse_lazy("rcs_2:info-create")


class ArduinoCreateView(CreateView):
    """
    Создание Arduino и какая-то информация о ней
    """
    model = Arduino
    fields = "name", "temperature_info", "station"
    template_name = 'rcs_2/arduino-create.html'
    success_url = reverse_lazy("rcs_2:arduino-create")


class MicrocomputerCreateView(CreateView):
    """
    Создание микрокомпьютера и какая-то информация о ней
    """
    model = Microcomputer
    fields = "name", "temperature_info", "station"
    template_name = 'rcs_2/micro-create.html'
    success_url = reverse_lazy("rcs_2:micro-create")

class MicrocomputerListView(ListView):
    """
    Список микрокомпьютеров
    """
    template_name = "rcs_2/micro-list.html"
    context_object_name = "microcomputers"
    queryset = Microcomputer.objects.all()


class ArduinoListView(ListView):
    """
    Список Arduino
    """
    template_name = "rcs_2/arduino-list.html"
    context_object_name = "arduinos"
    queryset = Arduino.objects.all()


def usb_web(request: HttpRequest) -> HttpResponse:
    """
    Информация с Arduino
    """
    with open("arduino.csv", "r", encoding="utf-8") as file:
        for line in file.read().split("\n"):  # Про тестить maxsplit, что бы произвести разделение на несколько строк
            name = line.strip().split(",")
            Sensor_Data.objects.create(name=name)
            data_sensor = [
                ("", line)
            ]
            context = {
                "data_sensor": data_sensor,
            }
            return render(request, "rcs_2/info-arduino.html", context=context)


class DataSensorListView(ListView):
    """
    Информаця с Arduino для анализа
    и работы с этими данными
    """
    template_name = "rcs_2/info-arduino.html"
    context_object_name = "Sensor_datas"
    queryset = Sensor_Data.objects.all()