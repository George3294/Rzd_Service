# Generated by Django 5.0.6 on 2024-10-16 08:18

import rcs_1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcs_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='documents',
            field=models.FileField(blank=True, null=True, upload_to=rcs_1.models.product_document_directory_path),
        ),
    ]
