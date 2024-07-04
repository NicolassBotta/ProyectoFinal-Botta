from django.db import models
from django.contrib.auth.models import User



class revista(models.Model):
    editorial = models.CharField(max_length=30)
    titulo = models.CharField(max_length=100)
    nombre_del_duenio = models.CharField(max_length=20)
    apellido_del_duenio = models.CharField(max_length=20)
    telefono_del_duenio = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='revistas/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class libro(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=20)
    nombre_del_duenio = models.CharField(max_length=20)
    apellido_del_duenio = models.CharField(max_length=20)
    telefono_del_duenio = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='libros/', blank=True, null=True)

    def __str__(self):
        return self.nombre
    

from django.db import models

class Comentario(models.Model):
    usuario = models.CharField(max_length=100)
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    seccion = models.CharField(max_length=10 ) 

    def __str__(self):
        return f'{self.usuario} - {self.fecha_comentario}'