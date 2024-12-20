# Generated by Django 5.0.6 on 2024-10-16 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arduinoapp', '0003_station_documents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
