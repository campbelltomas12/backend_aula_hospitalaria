from django.db import models

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    coordinador = models.ForeignKey('personas.Coordinador', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table = "sedes"

        
class Matricula(models.Model):
    folio = models.CharField(max_length=50)
    fecha = models.DateField()
    observaciones = models.TextField()
    semestre = models.CharField(max_length=50)
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True)
    alumno = models.ForeignKey('personas.Alumno', on_delete=models.CASCADE)
    diagnostico = models.ForeignKey('programa.Diagnostico', on_delete=models.SET_NULL, null=True)

class ProgresoAlumno(models.Model):
    anio = models.IntegerField()
    estado_aprobacion = models.CharField(max_length=50)
    curso = models.ForeignKey('academico.Curso', on_delete=models.CASCADE)
    alumno = models.ForeignKey('personas.Alumno', on_delete=models.CASCADE)

class NotasAlumno(models.Model):
    nota = models.FloatField()
    fecha_nota = models.DateField()
    asignatura = models.ForeignKey('academico.Asignatura', on_delete=models.CASCADE)
    curso = models.ForeignKey('academico.Curso', on_delete=models.CASCADE)
    alumno = models.ForeignKey('personas.Alumno', on_delete=models.CASCADE)