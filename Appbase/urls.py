from django.urls import path
from Appbase.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', about, name='about'),
    path('Productos/', products, name='productos'),
    path('Tienda/', store, name='tienda'),
    path("login", log_in, name = "login"),
    path("registro", registro, name = "registrar"),
]
