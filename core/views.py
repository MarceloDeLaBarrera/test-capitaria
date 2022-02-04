from django.db.models import Avg
from django.shortcuts import render
from core.models import Alumno, Alumno_Curso, Alumno_Curso_Prueba, Profesor, Prueba, Curso

# Create your views here.


def mostrar_alumnos(request):
    alumnos = Alumno.objects.all().order_by("nombre")
    context = {"alumnos": alumnos}
    return render(request, 'alumnos.html', context)


def mostrar_cursos(request):
    cursos = Curso.objects.all().order_by("nombre_curso")
    context = {"cursos": cursos}
    return render(request, 'cursos.html', context)


def mostrar_pruebas(request):
    pruebas = Prueba.objects.all().order_by("nombre_prueba")
    context = {"pruebas": pruebas}
    return render(request, 'pruebas.html', context)


def mostrar_notas(request):
    notas = Alumno_Curso.objects.get_or_create()
    notas2 = notas.alumno_curso_prueba_set.all()
    context = {"notas": notas}
    return render(request, 'notas.html', context)


def listar_promedionotas(request):
    querysett = Alumno_Curso_Prueba.objects.values(
        "alumno_curso__alumno__nombre", "alumno_curso__curso__nombre_curso").annotate(Avg("nota"))
    queryset = list(querysett)
    context = {"queryset": queryset}

    return render(request, 'listarpromedionotas.html', context)
