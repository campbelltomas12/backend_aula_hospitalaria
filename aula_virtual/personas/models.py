
from django.db import models


# Acá definimos el objeto Persona que será abstracto, es decir, no se creará una tabla en la base de datos para este modelo.
class Persona(models.Model):
    rut = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    class Meta:
        abstract = True
        

# Acá definimos los modelos que heredan de Persona y heredan todos sus campos.
class Apoderado(Persona):
    pass

class Alumno(Persona):
    fecha_nacimiento = models.DateField()
    colegio_origen = models.CharField(max_length=200)
    apoderado = models.ForeignKey(Apoderado, on_delete=models.SET_NULL, null=True)
    

class Coordinador(Persona):
    fecha_nacimiento = models.DateField()

class Docente(Persona):
    fecha_nacimiento = models.DateField()
    sede = models.ForeignKey('administrativo.Sede', on_delete=models.SET_NULL, null=True)
    
