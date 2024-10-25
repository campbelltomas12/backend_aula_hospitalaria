from django.db import models

class MotivoClase(models.Model):
    descripcion_motivo = models.TextField()

class RegistroClase(models.Model):
    fecha_registro = models.DateTimeField(auto_now_add=True)
    tipo_clase = models.ForeignKey('academico.TipoClase', on_delete=models.CASCADE)
    calificacion_docente = models.ForeignKey('academico.CalificacionDocente', on_delete=models.SET_NULL, null=True)
    alumno = models.ForeignKey('personas.Alumno', on_delete=models.CASCADE)
    motivo_cierre = models.ForeignKey(MotivoClase, on_delete=models.SET_NULL, null=True)
    docente = models.ForeignKey('personas.Docente', on_delete=models.SET_NULL, null=True)
    
class RegistroAsignatura(models.Model):
    alumno = models.ForeignKey('personas.Alumno', on_delete=models.CASCADE)
    docente = models.ForeignKey('personas.Docente', on_delete=models.SET_NULL, null=True)
    asignatura = models.ForeignKey('academico.Asignatura', on_delete=models.CASCADE)

class Comuna(models.Model):
    nombre = models.CharField(max_length=200)

class Region(models.Model):
     nombre = models.CharField(max_length=200)
    
    
    
    
    