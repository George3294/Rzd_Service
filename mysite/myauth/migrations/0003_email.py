# Generated by Django 5.0.6 on 2024-08-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0002_profile_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]