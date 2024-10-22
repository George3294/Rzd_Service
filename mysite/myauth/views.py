from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.views import LogoutView
# Create your views here.

class AboutView(ListView):
    """
    Информация о пользователе
    """
    template_name = "myauth/about-me.html"
    form_class = ProfileForm
    queryset = Profile.objects.all()


class AdditionalInformation(ListView):
    """
    Дополнительная информация о пользователе
    """
    model = Profile
    template_name = "myauth/additional_information.html"
    context_object = "profiles"
    queryset = Profile.objects.all()
class RegisterView(CreateView):
    """
    Регистрация пользователя
    """
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy('myauth:about-me')

    def form_valid(self, form):
        """
        Проверка на валидность регистрации
        :param form:
        :return:
        """
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")

        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class UpdateUserProfile(UpdateView):
    """
    Обновление профиля пользователя
    """
    model = Profile
    fields = "user","name","position", "document"
    template_name = "myauth/user-profile-update.html"
    #success_url = reverse_lazy('myauth:about-me')



def logout_view(request):
    """
    Выход с сайта
    :param request:
    :return:
    """
    logout(request)
    return redirect('myauth:login')
