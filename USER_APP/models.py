from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    uau = models.CharField(max_length=500, null=True)
    is_login = models.BooleanField(null=True) 
    is_working = models.BooleanField(null=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

