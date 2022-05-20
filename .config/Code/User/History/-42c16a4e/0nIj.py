from django.db import models

# Create your models here.

class ClientProfile():
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    fname = models.CharField(max_length=30, null=True, blank=True)
    lname = models.CharField(max_length=30)
    

    