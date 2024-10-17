from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Programa, HojaDeVida, Diagnostico
from .serializers import ProgramaSerializer, HojaDeVidaSerializer, DiagnosticoSerializer

@api_view(['GET', 'POST'])
def programa_list(request):
    if request.method == 'GET':
        programas = Programa.objects.all()
        serializer = ProgramaSerializer(programas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProgramaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def programa_detail(request, pk):
    try:
        programa = Programa.objects.get(pk=pk)
    except Programa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProgramaSerializer(programa)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProgramaSerializer(programa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        programa.delete()
        return Response({"mensaje": f"Programa ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def hoja_de_vida_list(request):
    if request.method == 'GET':
        hojas_de_vida = HojaDeVida.objects.all()
        serializer = HojaDeVidaSerializer(hojas_de_vida, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HojaDeVidaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def hoja_de_vida_detail(request, pk):
    try:
        hoja_de_vida = HojaDeVida.objects.get(pk=pk)
    except HojaDeVida.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HojaDeVidaSerializer(hoja_de_vida)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HojaDeVidaSerializer(hoja_de_vida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        hoja_de_vida.delete()
        return Response({"mensaje": f"HojaDeVida ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def diagnostico_list(request):
    if request.method == 'GET':
        diagnosticos = Diagnostico.objects.all()
        serializer = DiagnosticoSerializer(diagnosticos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DiagnosticoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def diagnostico_detail(request, pk):
    try:
        diagnostico = Diagnostico.objects.get(pk=pk)
    except Diagnostico.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DiagnosticoSerializer(diagnostico)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DiagnosticoSerializer(diagnostico, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        diagnostico.delete()
        return Response({"mensaje": f"Diagnostico ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)