from django import forms
from .models import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import User



class FormularioDeRegistroDeUsuario(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')


class FormularioDeEdicionDeUsuario(UserChangeForm):

    password = None
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')
    

class FormularioDeCambioDeContra(PasswordChangeForm):
    old_password = forms.CharField(label=("Contraseña actual"),widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nueva Contraseña"),widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita la nueva Contraseña"),widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class RevistaForm(forms.ModelForm):
    class Meta:
        model = revista
        fields = ['editorial', 'titulo', 'nombre_del_duenio', 'apellido_del_duenio', 'telefono_del_duenio', 'imagen']

class LibroForm(forms.ModelForm):
    class Meta:
        model = libro
        fields = ['nombre', 'autor', 'nombre_del_duenio', 'apellido_del_duenio', 'telefono_del_duenio', 'imagen']