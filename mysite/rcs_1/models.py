from django.db import models
from django.utils import timezone
# Create your models here.

def product_document_directory_path(instance: "Station", filename: str) -> str:
    return "station/station_{pk}/documents/{filename}".format(
        pk=instance,
        filename=filename,
    )

class Station(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100) # Station name
    temperature_info = models.CharField(max_length=100) # Station temperature info
    data_created = models.DateTimeField(default=timezone.now)
    documents = models.FileField(null=True, blank=True, upload_to=product_document_directory_path)

    def __str__(self):
        return self.name # Station name

    class Meta:
        verbose_name = 'Stations' # Station name
class Arduino(models.Model):
    """
    Модель Arduino предоставляет информацию о состоянии
    темперартуры на станции
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    temperature_info = models.IntegerField(default=0)
    update_data = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Arduino' # Arduino name

class Microcomputer(models.Model):
    """
    Модель Microcomputer предоставляет информацию о состоянии
    темперартуры на станции
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    temperature_info = models.IntegerField(default=0)
    update_data = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Microcomputer'  # Microcomputer name


class Sensor_Data(models.Model):
    """"
    Модель Sensor_Data предоставляет
    информацию о температуре на станции
    """
    name = models.CharField(max_length=200)
    temperature_info = models.IntegerField(default=0)