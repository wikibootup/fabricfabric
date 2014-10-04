from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from server.views import PublicIPView

from fabricfabric.views import Home
import server.views

urlpatterns = patterns('',
#    url(r'^$', server.views.index, name='index'),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^public_ip/', PublicIPView.as_view(), name="public_ip"),

)

