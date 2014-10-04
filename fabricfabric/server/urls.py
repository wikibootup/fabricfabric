from django.conf.urls import patterns, include, url
from django.views import Uname

from django.shortcuts import render
from django.http import HttpResponse

from server.views import PublicIPView

# Create your views here.
def index(request):
    return HttpResponse('Hello')
"""
urlpatterns = patterns('',
    url(r'^public_ip/', PublicIPView.as_view(), name="public_ip"),
)
"""

