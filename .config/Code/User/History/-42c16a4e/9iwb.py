from secrets import choice
from sre_constants import MAX_REPEAT
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class ClientProfile(models.Model):

    email = models.EmailField(db_column='email', max_length=255, unique=True, null=True, blank=True)
    fname = models.CharField(db_column='fname', max_length=30, null=True, blank=True)
    lname = models.CharField(db_column='lname', max_length= 30, null=True)

    homephone = models.CharField(db_column='homephone', max_length=15, blank=True, null=True)

    phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="")
    cellphone = models.CharField(db_column='cellphone',validators=[phone_validator],
                             max_length=17, blank=True,null=True)

    OFFICE_CHOICES = (
        (0, "RE/MAX México"),
    )

    ORIGIN_CHOICES = (
        (0, 'SIR || Tarjeta Digital'),
    )

    AGENT_CHOICES = (
        (0, 'Dinorah Felgueres Hernández'),
        (1, 'Eduardo Cruz García'),
        (2, 'Felipe Gonzalez Rosales'),
        (3, 'Salvador Haro Cisneros'),
    )

    STATUS_CHOICES = (
        (True, 'Activo'),
        (False, 'Inactivo'),
    )
    
    TYPE_CHOICES = (
        (0, 'Tipo 1'),
        (1, 'Tipo 2'),
    )

    office = models.CharField(max_length=20, choices=OFFICE_CHOICES, default=0)
    origin = models.CharField(max_length=20, choices=ORIGIN_CHOICES, default=0)
    agent = models.CharField(max_length=20, choices=AGENT_CHOICES, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=False)
    typeof = models.CharField(max_length=20, choices=TYPE_CHOICES, default=0)

    notes = models.TextField()