from django.urls import path
from .views import handel_file_upload, process_get_view, user_form

app_name = 'requestdataapp'
urlpatterns = [
    path("get/", process_get_view, name="request-query-params"),
    path("upload/", handel_file_upload, name="file-upload"),
    path("bio/", user_form, name="user-bio-form"),
]