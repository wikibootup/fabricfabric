from django.shortcuts import render
from django.http import HttpResponse

from django.conf.urls import patterns, url

# Create your views here.
def index(request):
    return HttpResponse('This is fabric test')

    

