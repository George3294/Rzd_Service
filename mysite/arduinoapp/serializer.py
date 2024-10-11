from rest_framework import serializers
from .models import Station, Sensor_Data, Arduino

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        Fields = (
            "pk",
            "name",
            "temperature_info",
            "data_created",
        )

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor_Data
        fields = (
            "name",
            "temperature_info",
        )

class ArduinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arduino
        fields = (
            "pk",
            "name",
            "station",
            "temperature_info",
            "update_data",
        )