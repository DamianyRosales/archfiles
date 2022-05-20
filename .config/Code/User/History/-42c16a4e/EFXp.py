from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class ClientProfile():
    email = models.EmailField(db_column='email', max_length=255, unique=True, null=True, blank=True)
    fname = models.CharField(db_column='fname', max_length=30, null=True, blank=True)
    lname = models.CharField(db_column='lname', max_length= 30, null=True)

    homephone = models.CharField(db_column='homephone', max_length=15, blank=True, null=True)

    phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="")
    cellphone = models.CharField(db_column='cellphone',validators=[phone_validator],
                             max_length=17, blank=True,null=True)


    