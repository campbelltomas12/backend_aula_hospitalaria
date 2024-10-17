from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sede, Matricula, ProgresoAlumno, NotasAlumno
from .serializers import SedeSerializer, MatriculaSerializer, ProgresoAlumnoSerializer, NotasAlumnoSerializer
from personas.models import Persona, Alumno
from personas.serializers import AlumnoSerializer, ApoderadoSerializer

@api_view(['GET', 'POST'])
def sede_list(request):
    if request.method == 'GET':
        sedes = Sede.objects.all()
        serializer = SedeSerializer(sedes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SedeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def sede_detail(request, pk):
    try:
        sede = Sede.objects.get(pk=pk)
    except Sede.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SedeSerializer(sede)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SedeSerializer(sede, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sede.delete()
        return Response({"mensaje": f"Sede ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)
    
@api_view(['GET', 'POST'])
def matricula_list(request):
    if request.method == 'GET':
        matriculas = Matricula.objects.all()
        respuesta = []

        serializer = MatriculaSerializer(matriculas, many=True)
        for matricula in serializer.data:
            alumno = Alumno.objects.get(pk=matricula['alumno'])
            serializer_alumno = AlumnoSerializer(alumno)
            matricula['info_alumno'] = serializer_alumno.data
            respuesta.append(matricula)
        return Response(respuesta)

    elif request.method == 'POST':
        # Guardar Alumno
        print("Datos del alumno:", request.data['info_alumno'])
        serializer_alumno = AlumnoSerializer(data=request.data['info_alumno'])
        if serializer_alumno.is_valid():
            alumno = serializer_alumno.save()
            print(f"Alumno guardado con ID: {alumno.id}")
        else:
            print("Errores en AlumnoSerializer:", serializer_alumno.errors)
            return Response(serializer_alumno.errors, status=status.HTTP_400_BAD_REQUEST)

        # Guardar Apoderado
        print("Datos del apoderado:", request.data['info_apoderado'])
        serializer_apoderado = ApoderadoSerializer(data=request.data['info_apoderado'])
        if serializer_apoderado.is_valid():
            apoderado = serializer_apoderado.save()
            print(f"Apoderado guardado con ID: {apoderado.id}")
        else:
            print("Errores en ApoderadoSerializer:", serializer_apoderado.errors)
            return Response(serializer_apoderado.errors, status=status.HTTP_400_BAD_REQUEST)

        # Guardar Matrícula
        request.data['alumno'] = alumno.id
        request.data['apoderado'] = apoderado.id
        serializer = MatriculaSerializer(data=request.data)

        if serializer.is_valid():
            matricula = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Errores en MatriculaSerializer:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'POST'])
# def matricula_list(request):
#     if request.method == 'GET':
#         matriculas = Matricula.objects.all()
#         respuesta=[]       
            
#         serializer = MatriculaSerializer(matriculas, many=True)
#         for matricula in serializer.data:
#             alumno=Alumno.objects.get(pk=matricula['alumno'])
#             serializer_alumno=AlumnoSerializer(alumno)
#             matricula['info_alumno']=serializer_alumno.data
#             respuesta.append(matricula)
#         return Response(respuesta)
    # elif request.method == 'POST':
    #     print(request.data['info_alumno'])
    #     serializer_alumno = AlumnoSerializer(data=request.data['info_alumno'])
    #     print(serializer_alumno.is_valid())
    #     if serializer_alumno.is_valid():
    #         serializer_alumno.save()
        
    #         print(serializer_alumno.data['id'])
    #     return
    #     serializer_apoderado = ApoderadoSerializer(data=request.data['info_apoderado'])
    #     if serializer_apoderado.is_valid():
    #        serializer_apoderado.save()
            
    #     serializer = MatriculaSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def matricula_detail(request, pk):
    try:
        matricula = Matricula.objects.get(pk=pk)
    except Matricula.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MatriculaSerializer(matricula)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MatriculaSerializer(matricula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        matricula.delete()
        return Response({"mensaje": f"Matricula ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def progreso_alumno_list(request):
    if request.method == 'GET':
        progresos = ProgresoAlumno.objects.all()
        serializer = ProgresoAlumnoSerializer(progresos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProgresoAlumnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def progreso_alumno_detail(request, pk):
    try:
        progreso = ProgresoAlumno.objects.get(pk=pk)
    except ProgresoAlumno.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProgresoAlumnoSerializer(progreso)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProgresoAlumnoSerializer(progreso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        progreso.delete()
        return Response({"mensaje": f"ProgresoAlumno ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def notas_alumno_list(request):
    if request.method == 'GET':
        notas = NotasAlumno.objects.all()
        serializer = NotasAlumnoSerializer(notas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NotasAlumnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def notas_alumno_detail(request, pk):
    try:
        nota = NotasAlumno.objects.get(pk=pk)
    except NotasAlumno.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotasAlumnoSerializer(nota)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = NotasAlumnoSerializer(nota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        nota.delete()
        return Response({"mensaje": f"NotasAlumno ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)