from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class Cursoformulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()

class EstudianteForm(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    

class ProfesorForm(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class UserEditForm(UserChangeForm):

    password = None
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Ingrese su email: ")
    

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name']

class Avatarformulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ('imagen',)