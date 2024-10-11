from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from .admin_mixins import ExportAsCSVMixin
from .models import Station, Arduino, Sensor_Data


#admin.site.register(Station)
#admin.site.register(Arduino)
#admin.site.register(Sensor_Data)


@admin.action(description="Archived station")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)

@admin.action(description="Unarchived station")
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)
@admin.register(Station)
class StationAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",
    ]
    list_display = "pk", "name", "temperature_info", "data_created"
    list_display_links = "pk", "name"
    search_fields = "name", "data_created"
    fieldsets = [
        ("Station",{
            "fields": ("name", "temperature_info", "data_created"),
        }),

    ]

@admin.register(Arduino)
class ArduinoAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",
    ]

@admin.register(Sensor_Data)
class Sensor_DataAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",
        "export_txt"
    ]