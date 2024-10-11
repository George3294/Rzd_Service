from django import forms
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.utils import validate_file_name


class UserBioForm(forms.Form):
    name = forms.CharField(max_length=100)
    position = forms.CharField(max_length=100)

class UploadForm(forms.Form):
    file = forms.FileField(validators=[validate_file_name])