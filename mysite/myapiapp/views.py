from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView
import serial
from django.contrib.auth.models import User


# Create your views here.


@api_view()
def hello_world(request):
    return Response({'hello': 'world'})