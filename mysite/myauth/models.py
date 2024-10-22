from django.db import models
from django.contrib.auth.models import User
# Create your models here.


def info_arduino_directory_path(instance: "Profile", filename: str) -> str:
    return "profiles/profile_{user}/documents/{filename}".format(
        user=instance.user.pk,
        filename=filename,
    )
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100)
    document = models.FileField(null=True, blank=True, upload_to=info_arduino_directory_path)
class Email(models.Model):
    email = models.EmailField(max_length=100)