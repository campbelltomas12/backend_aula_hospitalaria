from rest_framework import serializers
from .models import Programa, HojaDeVida, Diagnostico

class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = '__all__'

class HojaDeVidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HojaDeVida
        fields = '__all__'

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = '__all__'


