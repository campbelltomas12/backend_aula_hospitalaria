from rest_framework import serializers
from .models import Sede, Matricula, ProgresoAlumno, NotasAlumno

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ProgresoAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoAlumno
        fields = '__all__'

class NotasAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotasAlumno
        fields = '__all__'