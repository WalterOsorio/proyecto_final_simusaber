from django.contrib import admin
from .models import Estudiante, TipoDocumento, Usuario, UsuarioPrueba

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(TipoDocumento)
admin.site.register(Usuario)