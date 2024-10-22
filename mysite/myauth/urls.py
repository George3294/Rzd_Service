from django.contrib.auth.views import LoginView
from django.urls import path
from .views import AboutView, RegisterView, UpdateUserProfile, logout_view, AdditionalInformation

app_name = 'myauth'


urlpatterns = [
    path("login/",
          LoginView.as_view(
              template_name="myauth/login.html",
              redirect_authenticated_user=True), name="login"),
    path('logout/', logout_view, name='logout'),
    path('about/', AboutView.as_view(), name='about-me'),
    path('additional-info/', AdditionalInformation.as_view(), name='additional_information'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/<pk>update-profile', UpdateUserProfile.as_view(), name='user-profile-update'),

]
