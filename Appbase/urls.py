from re import template
from django.urls import path
from Appbase.views import *
from Appbase import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    #html:
    path('', inicio, name='inicio'),
    path('about/', about, name='about'),
    path('Productos/', products, name='productos'),
    path('Tienda/', store, name='tienda'),
    

    #registro-login-perfiles:
    path("login", log_in, name = "login"),
    path("registro", registro, name = "registrar"),
    path("logout", LogoutView.as_view(template_name='registro-login-perfiles/logout.html'), name = "logout"),
    path("editarperfil", editarperfil, name = "editaperfil"),
    path("cambiarcontrasenia", views.Cambiarcontrasenia.as_view(), name = "Cambiarcontrasenia"),

    #Revistas
    path("Revistas/lista", views.RevistaListView.as_view(), name = "ListaRevistas"),
    path("Revistas/crear", views.RevistaCreateView.as_view(), name = "CrearRevista"),
    path("Revistas/<pk>", views.RevistadetailView.as_view(), name = "DetalleRevista"),
    path("Revistas/<pk>/editar", views.RevistaUpdateView.as_view(), name = "EditarRevista"),
    path("Revistas/<pk>/borrar", views.RevistaDeleteView.as_view(), name = "BorrarRevista"),

    #Libros
    path("Libros/lista", views.LibroListView.as_view(), name = "ListaLibros"),
    path("Libros/crear", views.LibroCreateView.as_view(), name = "CrearLibro"),
    path("Libros/<pk>", views.LibroDetailView.as_view(), name = "DetalleLibro"),
    path("Libros/<pk>/editar", views.LibroUpdateView.as_view(), name = "EditarLibro"),
    path("Libros/<pk>/borrar", views.LibroDeleteView.as_view(), name = "BorrarLibro"),

    #Foro
    path('guardar_comentario/', views.guardar_comentario, name='guardar_comentario'),
    path('productos/', views.productos, name='productos'),
]
