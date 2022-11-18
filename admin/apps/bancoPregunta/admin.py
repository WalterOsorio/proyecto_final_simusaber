from django.contrib import admin
from .models import BancoPregunta, PruebaBancoPregunta, Resultado, Retroalimentacion

# Register your models here.

admin.site.register(BancoPregunta)
admin.site.register(PruebaBancoPregunta)
admin.site.register(Resultado)
admin.site.register(Retroalimentacion)