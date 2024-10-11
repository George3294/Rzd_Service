# Generated by Django 5.0.6 on 2024-06-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arduinoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('temperature_info', models.IntegerField(default=0)),
            ],
        ),
    ]