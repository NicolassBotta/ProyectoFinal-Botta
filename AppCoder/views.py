
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from .models import curso, estudiante, profesor, Avatar
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView



def crea_curso(req, nombre, camada):

    nuevo_curso = curso(nombre=nombre, camada=camada)

    nuevo_curso.save()
    

    return HttpResponse(f"""
        <p>curso: {nuevo_curso.nombre} - camada: {nuevo_curso.camada} creado</p>
    """)

def lista_cursos(req):
    lista = curso.objects.all()

    return render(req, "lista_cursos.html", {"lista_cursos" : lista})

def inicio(req):

    avatar = Avatar.objects.get(user=req.user.id)

    return render(req, "inicio.html",{"url": avatar.imagen.url})


class CursoListView(LoginRequiredMixin, ListView):
    model = curso
    template_name = 'curso_list.html'
    context_object_name = "cursos"

class CursoDetailView(DetailView):
    model = curso
    template_name = "curso_detalle.html"

class CursoCreateView(CreateView):
    model = curso
    template_name = "curso_crear.html"
    success_url = reverse_lazy('Listacursos')
    fields = ['nombre', 'camada']

class CursoUpdateView(UpdateView):
    model = curso
    template_name = "curso_editar.html"
    success_url = reverse_lazy('Listacursos')
    fields = ['nombre','camada']

class CursoDeleteView(DeleteView):
    model = curso
    template_name = "curso_borrar.html"
    success_url = reverse_lazy('Listacursos')

def cursoformulario(req):

    if req.method == 'POST':

        miFormulario = Cursoformulario(req.POST) 

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            nuevo_curso = curso(nombre=data['curso'], camada=data['camada'])
            nuevo_curso.save()

            return render(req, "inicio.html",{"message": "curso creado con exito"})
        else:
            return render(req, "inicio.html",{"message": "datos invalidos"})
    else:

        miFormulario = Cursoformulario()

        return render(req, "curso_formulario.html",{"miFormulario": miFormulario})

def estudiantes(req):

    return render(req, "estudiantes.html",{})

def profesores(req):
    profes = profesor.objects.all()

    contexto = {"profesores": profes}

    return render(req,"profesores.html", contexto)

def eliminar_profesor(req, profesor_nombre):

    Profesor = profesor.objects.get(nombre=profesor_nombre)
    Profesor.delete()
    
    mis_profesores = profesor.objects.all()
    contexto = {"profesores": mis_profesores}

    return render(req,"profesores.html", contexto)

def editarprofesor(req, profesor_nombre):
    
    Profesor = profesor.objects.get(nombre=profesor_nombre)
    if req.method == 'POST':

        miFormulario = ProfesorForm(req.POST) 

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data


            Profesor.nombre = data["nombre"]
            Profesor.apellido = data["apellido"]
            Profesor.email = data["email"]
            Profesor.profesion = data["profesion"]

            Profesor.save()

            return render(req, "inicio.html",{"message": "profesor actualizado con exito"})
        else:
            return render(req, "inicio.html",{"message": "datos invalidos"})
    else:

        miFormulario = ProfesorForm(initial={
            "nombre":Profesor.nombre,
            "apellido":Profesor.apellido,
            "email":Profesor.email,
            "profesion":Profesor.profesion,})

        return render(req, "EditarProfesor.html",{"miFormulario": miFormulario, "profesor_nombre":profesor_nombre})

def entregables(req):

    return render(req, "entregables.html",{})


    
    
def busquedacamada(req):

    return render(req, "busquedacamada.html",{})

def buscar(req):

    if req.GET["camada"]:
        
        camada= req.GET["camada"]

        cursos= curso.objects.filter(camada=camada)

        return render(req, "resultadobusqueda.html",{"cursos": cursos, "camada": camada})
    else:
        return render(req, "inicio.html",{"message": "no enviaste el numero de la camada"})


def estudianteformulario(req):
    if req.method == 'POST':

        miFormulario = EstudianteForm(req.POST) 

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            nuevoprofesor = estudiante(nombre=data["nombre"],apellido=data["apellido"])
            nuevoprofesor.save()

            return render(req, "inicio.html",{"message": "estudiante creado con exito"})
        else:
            return render(req, "inicio.html",{"message": "datos invalidos"})
    else:

        miFormulario = EstudianteForm()

        return render(req, "estudianteformulario.html",{"miFormulario": miFormulario})



def profesorformulario(req):
    if req.method == 'POST':

        miFormulario = ProfesorForm(req.POST) 

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            nuevoprofesor = profesor(nombre=data["nombre"],apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
            nuevoprofesor.save()

            return render(req, "inicio.html",{"message": "profesor creado con exito"})
        else:
            return render(req, "inicio.html",{"message": "datos invalidos"})
    else:

        miFormulario = ProfesorForm()

        return render(req, "profesorformulario.html",{"miFormulario": miFormulario})

def altologin(req):
    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data= req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            usuario = data["username"]
            contrasenia = data["password"]

            user = authenticate(username= usuario, password= contrasenia)

            if user is not None:
                login(req, user)
                return render(req,"inicio.html",{"message": f"Bienvenido {usuario}"})
            else:
                return render(req, "inicio.html",{"message": "Datos erroneos"})
            
        else:
            return render(req, "inicio.html",{"message": "   Datos invalidos"})
    else:

        miFormulario = AuthenticationForm()

        return render(req, "login.html",{"miFormulario": miFormulario})
    
def registro(req):
    if req.method == 'POST':

        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            usuario = data["username"]
            
            miFormulario.save()

            return render(req,"inicio.html",{"message": f"Usuario {usuario} creado"})
        else:
            return render(req, "inicio.html",{"message": "   Datos invalidos"})
    else:

        miFormulario = UserCreationForm()

        return render(req, "registro.html",{"miFormulario": miFormulario})
    
@login_required
def editarperfil(req):

    usuario = req.user

    if req.method == 'POST':

        miFormulario = UserEditForm(req.POST, instance=req.user) 

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

        miFormulario = UserEditForm(instance=req.user)


        return render(req, "editarperfil.html",{"miFormulario": miFormulario})
    
class Cambiarcontrasenia(LoginRequiredMixin,PasswordChangeView):
    template_name = 'cambiarcontra.html'
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
            return render(req, "inicio.html", {"message": "Avatar cargado con éxito"})
        else:
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    else:
        miFormulario = Avatarformulario()
        return render(req, "agregaravatar.html", {"miFormulario": miFormulario})