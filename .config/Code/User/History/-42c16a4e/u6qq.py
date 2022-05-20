from django.db import models

# Create your models here.

class ClientProfile():
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    