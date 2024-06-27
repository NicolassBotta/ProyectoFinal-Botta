from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from .models import cliente
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView


def inicio(request):
    return render(request, 'inicio.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'productos.html')

def store(request):
    return render(request, 'tienda.html')



def log_in(req):
    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data= req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            usuario = data["username"]
            contrasenia = data["password"]

            user = authenticate(username= usuario, password= contrasenia)

            if user is not None:
                login(req, user)
                return render(req,"padre.html",{"message": f"Bienvenido {usuario}"})
            else:
                return render(req, "padre.html",{"message": "Datos erroneos"})
            
        else:
            return render(req, "padre.html",{"message": "Datos invalidos"})
    else:

        miFormulario = AuthenticationForm()

        return render(req, "registro-login-perfiles/login.html",{"miFormulario": miFormulario})
    
def registro(req):
    if req.method == 'POST':

        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            usuario = data["username"]
            
            miFormulario.save()

            return render(req,"padre.html",{"message": f"Usuario {usuario} creado"})
        else:
            return render(req, "padre.html",{"message": "   Datos invalidos"})
    else:

        miFormulario = UserCreationForm()

        return render(req, "registro-login-perfiles/registro.html",{"miFormulario": miFormulario})