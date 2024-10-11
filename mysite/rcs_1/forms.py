from django import forms
from .models import Station, Arduino, Microcomputer

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = 'name', "temperature_info"


class ArduinoForm(forms.ModelForm):
    class Meta:
        model = Arduino
        fields = 'name', "temperature_info", "station"


class MicrocomputerForm(forms.ModelForm):
    class Meta:
        model = Microcomputer
        fields = 'name', "temperature_info", "station"