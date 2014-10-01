from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from fabricfabric.views import Home
from server.views import Logout
import server.views

urlpatterns = patterns('',
#    url(r'^$', server.views.index, name='index'),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^logout/', Logout.as_view(), name="logout"),    
)

