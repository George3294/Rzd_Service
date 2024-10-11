from django.urls import path
from .views import hello_world


app_name = 'myapiapp'


urlpatterns = [
    path('hello/', hello_world, name='hello'),
#    path('user/', UserListView.as_view(), name='user'),
#    path('usb/', usb_view, name='usb'),
]