# Generated by Django 5.0.6 on 2024-07-25 06:28

import arduinoapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arduinoapp', '0002_sensor_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='documents',
            field=models.FileField(blank=True, null=True, upload_to=arduinoapp.models.product_document_directory_path),
        ),
    ]
