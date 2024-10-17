from django.db import models

class Programa(models.Model):
    titulo = models.CharField(max_length=200)
    alumno = models.ForeignKey('personas.Alumno', on_delete=models.CASCADE)

class HojaDeVida(models.Model):
    promedio = models.FloatField()
    observacion = models.TextField()
    alumno = models.OneToOneField('personas.Alumno', on_delete=models.CASCADE)

class Diagnostico(models.Model):
    descripcion = models.TextField()
    estancia = models.CharField(max_length=100)
    alumno = models.ForeignKey('personas.Alumno', on_delete=models.CASCADE)
