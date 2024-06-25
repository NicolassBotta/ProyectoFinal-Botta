from django.db import models
from django.contrib.auth.models import User

class cliente(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=15)