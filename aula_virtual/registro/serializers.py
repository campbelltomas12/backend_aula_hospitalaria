from rest_framework import serializers
from .models import MotivoClase, RegistroClase

class MotivoClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotivoClase
        fields = '__all__'

class RegistroClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroClase
        fields = '__all__'