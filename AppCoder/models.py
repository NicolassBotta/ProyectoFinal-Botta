from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.camada}'

class estudiante(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"

class entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField

class Avatar(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null = True)