# Generated by Django 5.0.6 on 2024-07-17 11:51

import myauth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=myauth.models.info_arduino_directory_path),
        ),
    ]
