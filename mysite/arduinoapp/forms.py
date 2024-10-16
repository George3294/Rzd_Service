from django import forms
from .models import Station, Arduino, Image

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = "name", "temperature_info"
        
class ArduinoForm(forms.ModelForm):
    class Meta:
        model = Arduino
        fields = "name", "temperature_info", "station"


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')
