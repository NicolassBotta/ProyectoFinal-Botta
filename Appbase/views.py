from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.utils import timezone
from .models import Comentario


def inicio(request):
    return render(request, 'inicio.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'productos.html')

def store(request):
    return render(request, 'tienda.html')

#Registro-Login-Logout-Contrasenia-Avatar

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
                return render(req,"inicio.html",{})
            else:
                return render(req, "padre.html",{"message": "Datos erroneos"})
            
        else:
            return render(req, "padre.html",{"message": "Datos invalidos, vuelva al inicio"})
    else:

        miFormulario = AuthenticationForm()

        return render(req, "registro-login-perfiles/login.html",{"miFormulario": miFormulario})
    
def registro(req):
    if req.method == 'POST':
        miFormulario = FormularioDeRegistroDeUsuario(req.POST)  

        if miFormulario.is_valid():
            user = miFormulario.save()  
            username = miFormulario.cleaned_data.get('username')


            return render(req, "padre.html", {"message": f"Usuario {username} creado, vuelve al inicio para iniciar sesión."})
        else:
            return render(req, "padre.html", {"message": "Datos inválidos, vuelva al inicio"})
    else:
        miFormulario = FormularioDeRegistroDeUsuario()
        return render(req, "registro-login-perfiles/registro.html", {"miFormulario": miFormulario})
    

@login_required
def editarperfil(req):

    usuario = req.user

    if req.method == 'POST':

        miFormulario = FormularioDeEdicionDeUsuario(req.POST, instance=req.user) 

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data


            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]

            usuario.save()

            return render(req, "inicio.html",{"message": "Datos actualizados con exito"})
        else:
            return render(req, "inicio.html",{"message": "datos invalidos"})
    else:

        miFormulario = FormularioDeEdicionDeUsuario(instance=req.user)


        return render(req, "registro-login-perfiles/editarperfil.html",{"miFormulario": miFormulario})
    

class Cambiarcontrasenia(LoginRequiredMixin,PasswordChangeView):
    form_class = FormularioDeCambioDeContra
    template_name = 'registro-login-perfiles/cambiarcontra.html'
    success_url = reverse_lazy('editaperfil')


@login_required
def agregar_avatar(req):
    if req.method == 'POST':
        miFormulario = Avatarformulario(req.POST, req.FILES)
        
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            avatar, created = Avatar.objects.get_or_create(user=req.user)
            avatar.imagen = data["imagen"]
            avatar.save()
            return render(req, "padre.html", {"message": "Avatar cargado con éxito"})
        else:
            return render(req, "padre.html", {"message": "Datos inválidos"})
    else:
        miFormulario = Avatarformulario()
        return render(req, "registro-login-perfiles/agregaravatar.html", {"miFormulario": miFormulario})


#CRUD Revistas


class RevistaListView(LoginRequiredMixin, ListView):
    model = revista
    context_object_name = "Revistas"
    template_name = "revista_lista.html"

class RevistadetailView(LoginRequiredMixin, DetailView):
    model = revista
    template_name = "revista_detalle.html"

class RevistaCreateView(LoginRequiredMixin, CreateView):
    model = revista
    template_name = 'revista_crear.html'
    fields = ['editorial', 'titulo', 'telefono_del_duenio', 'imagen']
    success_url = reverse_lazy('ListaRevistas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user 
        return super().form_valid(form)

class RevistaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = revista
    template_name = "revista_editar.html"
    form_class = RevistaForm
    success_url = reverse_lazy('ListaRevistas')

    def test_func(self):
        revista = self.get_object()
        return self.request.user == revista.usuario

class RevistaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = revista
    template_name = "revista_borrar.html"
    success_url = reverse_lazy('ListaRevistas')

    def test_func(self):
        revista = self.get_object()
        return self.request.user == revista.usuario


#CRUD Libros

class LibroListView(LoginRequiredMixin, ListView):
    model = libro
    context_object_name = "Libros"
    template_name = "libro_lista.html"

class LibroDetailView(LoginRequiredMixin, DetailView):
    model = libro
    template_name = "libro_detalle.html"
    context_object_name = 'libro'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre_creador'] = self.object.usuario.username
        return context

class LibroCreateView(LoginRequiredMixin, CreateView):
    model = libro
    template_name = "libro_crear.html"
    form_class = LibroForm
    success_url = reverse_lazy('ListaLibros')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class LibroUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = libro
    template_name = "libro_editar.html"
    form_class = LibroForm
    success_url = reverse_lazy('ListaLibros')


    def test_func(self):
        libro = self.get_object()
        return self.request.user == libro.usuario

class LibroDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = libro
    template_name = "libro_borrar.html"
    success_url = reverse_lazy('ListaLibros')

    def test_func(self):
        libro = self.get_object()
        return self.request.user == libro.usuario


#Foro

@login_required
def guardar_comentario(request):
    if request.method == 'POST':
        comentario_texto = request.POST.get('comentario', '')
        seccion = request.POST.get('seccion', '')
        usuario = request.user.username 
        fecha_comentario = timezone.now()
        
        
        comentario = Comentario(usuario=usuario, texto=comentario_texto, fecha_comentario=fecha_comentario, seccion=seccion)
        comentario.save()
        
        return redirect('productos')  
    return redirect('productos') 

@login_required
def productos(request):
    comentarios1 = Comentario.objects.filter(seccion='1').order_by('-fecha_comentario')
    comentarios2 = Comentario.objects.filter(seccion='2').order_by('-fecha_comentario')  
    comentarios3 = Comentario.objects.filter(seccion='3').order_by('-fecha_comentario')  
    comentarios4 = Comentario.objects.filter(seccion='4').order_by('-fecha_comentario')
    comentarios5 = Comentario.objects.filter(seccion='5').order_by('-fecha_comentario')  
    comentarios6 = Comentario.objects.filter(seccion='6').order_by('-fecha_comentario')  
    comentarios7 = Comentario.objects.filter(seccion='7').order_by('-fecha_comentario')  
    
    context = {
        'comentarios1': comentarios1,
        'comentarios2': comentarios2,
        'comentarios3': comentarios3,
        'comentarios4': comentarios4,
        'comentarios5': comentarios5,
        'comentarios6': comentarios6,
        'comentarios7': comentarios7,
    }
    return render(request, 'productos.html', context)
