from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,StreamingHttpResponse

from django.conf.urls import patterns, url

from django.views.generic.edit import FormView
from server.forms import PublicIPForm

from django.core.urlresolvers import reverse

from django.core.exceptions import ValidationError
from django.contrib import messages

import subprocess

import os

external_IP = os.environ['BUILDBUILD_EX_IP']
internal_IP = os.environ['BUILDBUILD_IN_IP']

# Create your views here.
def index(request):
    return HttpResponse('This is fabric test')

class PublicIPView(FormView):
    template_name = "server/public_ip.html"
    form_class = PublicIPForm

    def form_valid(self, form):
        select_IP = self.request.POST["select_ip"]
        print self.request.POST.keys()  

#        msg = subprocess.check_output(["fab", "host_type"])
#        msg = msg.replace(external_IP, 'buildbuild external IP')
        return HttpResponse(select_IP)
