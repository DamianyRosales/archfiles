from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class ClientProfile():
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    fname = models.CharField(max_length=30, null=True, blank=True)
    lname = models.CharField(max_length= 30, null=True)
    phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="")
    
    