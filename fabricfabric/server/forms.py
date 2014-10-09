from django import forms
import os

external_IP = 'ex_ip'
internal_IP = 'in_ip'

mapping_IP = (
    (external_IP, "External IP"),
    (internal_IP, "Internal IP"),
#    (external_IP, os.environ['BUILDBUILD_EX_IP']),
#    (internal_IP, os.environ['BUILDBUILD_IN_IP']),
)

class PublicIPForm(forms.Form):
    select_ip = forms.ChoiceField(
        required=True, 
        widget=forms.RadioSelect(),
        choices = mapping_IP,
        label=""
    )

