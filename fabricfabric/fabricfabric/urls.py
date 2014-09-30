from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from fabricfabric.views import Home
import server.views

urlpatterns = patterns('',
#    (r'^home/', TemplateView.as_view(template_name="home.html")),        
#    url(r'^$', server.views.index, name='index'),
    url(r'^$', Home.as_view(), name='home'),
)

