from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User






class UserEditForm(UserChangeForm):

    password = None
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Ingrese su email: ")
    

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name']
