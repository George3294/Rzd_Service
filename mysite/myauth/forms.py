from django import forms
from myauth.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProfileForm(forms.ModelForm):
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    class Meta:
        models = Profile
        fields = "username", "last_name", "password1", "password2"
    document = forms.FileField(
        widget=forms.ClearableFileInput(),
    )