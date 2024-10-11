from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.files.storage import FileSystemStorage
# Create your views here.


def process_get_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get("a", "Привет!!!")
    b = request.GET.get("b", "Друг!!!")
    result = a + b
    context = {
        "a": a,
        "b": b,
        "result": result,
    }
    return render(request, "requestdataapp/request-query-params.html", context = context)


def handel_file_upload(request: HttpRequest) -> HttpResponse:
    if request.method == "POST" and request.FILES.get("data.txt"):
        myfile = request.FILES["data.txt"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        file_size = fs.size(filename)
        if file_size > 10485787:
            fs.delete(filename)
            print("Файл удален!!!", filename)
            return render(request, "requestdataapp/error-messages.html")
        else:
            print("Файл сохранен!!!", filename)
    return render(request, "requestdataapp/file-upload.html")


def user_form(request: HttpRequest) -> HttpResponse:
    return render(request, "requestdataapp/user-bio-form.html")