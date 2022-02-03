from django.shortcuts import render
from core.models import Alumno, Alumno_Curso, Alumno_Curso_Prueba, Profesor, Prueba, Curso

# Create your views here.


def mostrar_alumnos(request):
    alumnos = Alumno.objects.all().order_by("name")
    context = {"alumnos": alumnos}
    return render(request, 'core/alumnos.html', context)


def mostrar_cursos(request):
    cursos = Curso.objects.all().order_by("name")
    context = {"cursos": cursos}
    return render(request, 'core/cursos.html', context)


def mostrar_pruebas(request):
    pruebas = Prueba.objects.all().order_by("name")
    context = {"pruebas": pruebas}
    return render(request, 'core/pruebas.html', context)


def mostrar_notas(request):
    notas = Alumno_Curso_Prueba.objects.all()
    context = {"notas": notas}
    return render(request, 'core/notas.html', context)
