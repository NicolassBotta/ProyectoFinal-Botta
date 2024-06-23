
from re import template
from django.urls import path
from AppCoder import views
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', crea_curso),
    path("listadecursos/", lista_cursos),
        path("inicio/", inicio, name = "Inicio"),
    path("estudiantes/", estudiantes, name = "Estudiantes"),
    path("profesores/", profesores, name = "Profesores"),
    path("entregables/", entregables, name = "Entregables"),
    path("curso-formulario/", cursoformulario, name = "Formulario"),
    path("busquedacamada/", busquedacamada, name="busquedacamada"),
    path("buscar/", buscar, name="buscar"),
    path('estudianteformulario/', estudianteformulario, name='estudianteformulario'),
    path('profesorformulario/', profesorformulario, name='profesorformulario'),
    path("borrarprofesor/<profesor_nombre>/", eliminar_profesor, name="borrarprofesores"),
    path("editarprofesor/<profesor_nombre>/", editarprofesor, name="EditarProfesor"),
    path("cursos/lista", CursoListView.as_view(), name = "Listacursos"),
    path("cursos/<pk>", CursoDetailView.as_view(), name = "Detallecursos"),
    path("cursos/nuevo", CursoCreateView.as_view(), name = "Creacursos"),
    path("cursos/<pk>/editar", CursoUpdateView.as_view(), name = "Editacursos"),
    path("cursos/<pk>/borrar", CursoDeleteView.as_view(), name = "Eliminacursos"),
    path("login", altologin, name = "login"),
    path("registro", registro, name = "registrar"),
    path("logout", LogoutView.as_view(template_name='logout.html'), name = "logout"),
    path("editarperfil", editarperfil, name = "editaperfil"),
    path("cambiarcontrasenia", views.Cambiarcontrasenia.as_view(), name = "Cambiarcontrasenia"),
    path("agregaravatar", agregar_avatar, name = "Agregaravatar"),
    
]
