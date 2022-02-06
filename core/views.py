from django.db.models import Avg, Count, Q
from django.shortcuts import render
from core.models import Alumno, Alumno_Curso, Alumno_Curso_Prueba, Profesor, Prueba, Curso

# Create your views here.


def mostrar_alumnos(request):
    alumnos = Alumno.objects.all().order_by("nombre")
    context = {"alumnos": alumnos}
    return render(request, 'alumnos/alumnos.html', context)


def mostrar_cursos(request):
    cursos = Curso.objects.all().order_by("nombre_curso")
    context = {"cursos": cursos}
    return render(request, 'cursos/cursos.html', context)


def mostrar_pruebas(request):
    pruebas = Prueba.objects.all().order_by("nombre_prueba")
    context = {"pruebas": pruebas}
    return render(request, 'pruebas/pruebas.html', context)


def mostrar_notas(request):
    notas = Alumno_Curso.objects.get_or_create()
    notas2 = notas.alumno_curso_prueba_set.all()
    context = {"notas": notas}
    return render(request, 'notas/notas.html', context)


def listar_promedionotas(request):
    queryset = Alumno_Curso_Prueba.objects.values(
        "alumno_curso__alumno__nombre", "alumno_curso__curso__nombre_curso").annotate(Avg("nota"))
    promedios_por_curso = list(queryset)

    promedio_menor_a_4 = Alumno_Curso_Prueba.objects.select_related(
        "alumno_curso", "prueba").values("alumno_curso__alumno__nombre", "alumno_curso__curso__nombre_curso").annotate(prom=Avg("nota")).filter(nota__lte=4).annotate(cnt=Count('alumno_curso__alumno__nombre')).filter(cnt__gte=2)

    context = {"queryset": promedios_por_curso,
               "queryset2": promedio_menor_a_4}
    return render(request, 'notas/listarpromedionotas.html', context)
