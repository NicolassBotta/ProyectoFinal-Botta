from django.db import models
from django.contrib.auth.models import User



class revista(models.Model):
    editorial = models.CharField(max_length=30)
    titulo = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    telefono_del_duenio = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='revistas/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    
class libro(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=20)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    telefono_del_duenio = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='libros/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    

class Comentario(models.Model):
    usuario = models.CharField(max_length=100)
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    seccion = models.CharField(max_length=10 ) 

    def __str__(self):
        return f'{self.usuario} - {self.fecha_comentario}'
    

class Avatar(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null = True)

    def __str__(self):
        return f'{self.user.username} Avatar'