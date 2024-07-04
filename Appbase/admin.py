from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(revista)
admin.site.register(libro)
admin.site.register(Comentario)