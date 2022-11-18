from django.db import models
from apps.states.models import Estado

class BancoPregunta(models.Model):
    
    nombre=models.CharField(max_length=225, null=True)
    descripcion=models.CharField(max_length=225, null=True)
    materia=models.ForeignKey('prueba.Materia', blank=True, on_delete=models.CASCADE, null=True)
    pregunta=models.CharField('Preguntas', max_length=45, null=True)
    grado=models.ForeignKey('prueba.Grado', blank=True, on_delete=models.CASCADE, null=True)
    estado=models.ForeignKey(Estado, blank=True, on_delete=models.CASCADE, null=True)   
    
    def __str__(self):
        return self.nombre
    

class Retroalimentacion(models.Model):
        
    nombre=models.CharField(max_length=225, null=True)
    descripcion=models.CharField(max_length=225, null=True)
    
    def __str__(self):
        return self.nombre
    

class Resultado(models.Model):
    
    nombre_resultado=models.CharField(max_length=45, null=True)
    retroalimentacion=models.ForeignKey(Retroalimentacion, blank=True, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nombre_resultado
    
class PruebaBancoPregunta(models.Model):
    
    prueba=models.ForeignKey('prueba.Prueba', blank=True, on_delete=models.CASCADE, null=True)
    banco_pregunta=models.ForeignKey(BancoPregunta, blank=True, on_delete=models.CASCADE, null=True)