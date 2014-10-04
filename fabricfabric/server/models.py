from django.db import models

"""
# Create your models here.
import os

class PublicIP(models.Model):
    external_IP = 'ex'
    internal_IP = 'in'
    
    mapping_IP = (
        (external_IP, os.environ['BUILDBUILD_EX_IP']),
        (internal_IP, os.environ['BUILDBUILD_IN_IP']),
    )
    
    select_IP = models.GenericIPAddressField(
        max_length=18,
        choices = mapping_IP,
        default = external_IP,
    ) 
"""
