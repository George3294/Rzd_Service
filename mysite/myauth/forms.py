from django import forms
from myauth.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        models = Profile
        fields = ["user", "name", "position"]
    document = forms.FileField(
        widget = forms.ClearableFileInput(),
    )