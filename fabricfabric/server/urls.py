from django.conf.urls import patterns, include, url
from django.views import Uname

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello')
