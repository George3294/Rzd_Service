from typing import Any
from django.http import HttpRequest, HttpResponse

def setup_useragent_on_request_middleware(get_response):
    print("initial call")
    def middleware(request: HttpRequest) -> HttpResponse:
        print("before get response")
        request.user_agent = request.META.get('HTTP_USER_AGENT')
        response = get_response(request)
        print("after get response")
        return response
    return middleware

class CountRequestsMiddleware:
    def __init__(self, get_response): # Создание экземпляра класса, вызывающего экземпляр класса
        self.get_response = get_response
        self.request_count = 0
        self.response_count = 0
        self.exception_count = 0

    def __call__(self, request: HttpRequest): # Вызов объекта экземпляра класса
        self.request_count += 1
        print("request count", self.request_count)
        response = self.get_response(request)
        self.response_count += 1
        print("response count", self.response_count)
        self.response_count += 1
        return response
    def proccess_exception(self, request: HttpRequest, exception: Exception):
        self.exception_count += 1
        print("got", self.exception_count, "exception so far")