from django.db import models

# Create your models here.

class TipoDocumento(models.Model):

    nombre_documento=models.CharField(max_length=45, null=True)
    
    def __str__(self):
        return self.nombre_documento


class Estudiante(models.Model):
        
    tipo_documento=models.ForeignKey(TipoDocumento, blank=True, on_delete=models.CASCADE, null=True)
    numero_documento=models.CharField(max_length=45, null=True)
    estado=models.ForeignKey('states.Estado', blank=True, on_delete=models.CASCADE, null=True) 
    grado=models.ForeignKey('prueba.Grado', blank=True, on_delete=models.CASCADE, null=True) 
    
    def __str__(self):
        return self.numero_documento


class Usuario(models.Model):   
    
    nombre=models.CharField('Nombres', max_length=45, null=True)
    email=models.EmailField(null=True)
    usuario=models.CharField(max_length=45, null=True)
    estudiante=models.ForeignKey(Estudiante, blank=True, on_delete=models.CASCADE, null=True)
    fecha_de_registro=models.DateField()
    
    def __str__(self):
        return self.nombre 


    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        db_table='usuario'


class UsuarioPrueba():
    
    usuario=models.ForeignKey(Usuario, blank=True, on_delete=models.CASCADE, null=True)
    prueba=models.ForeignKey('prueba.Prueba', blank=True, on_delete=models.CASCADE, null=True)