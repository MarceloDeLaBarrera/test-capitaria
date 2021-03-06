from django.db.models import Avg, Count
from django.shortcuts import redirect, render
from core.models import Alumno, Alumno_Curso_Prueba, Prueba, Curso
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

# Vistas Alumnos


def mostrar_alumnos(request):
    alumnos = Alumno.objects.all().order_by("nombre")
    context = {"alumnos": alumnos}
    return render(request, 'alumnos/alumnos.html', context)


def agregar_alumno(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    email = request.POST["email"]
    telefono = request.POST["telefono"]
    alumno = Alumno.objects.create(
        nombre=nombre, apellido=apellido, email=email, telefono=telefono)
    return redirect('alumnos')


def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    return render(request, "alumnos/editaralumno.html", {"alumno": alumno})


def actualizar_alumno(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    email = request.POST["email"]
    telefono = request.POST["telefono"]
    alumno = Alumno.objects.get(id=id)
    alumno.nombre = nombre
    alumno.apellido = apellido
    alumno.email = email
    alumno.telefono = telefono
    alumno.save()
    return redirect('alumnos')


def eliminar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect('alumnos')


# Vistas Notas

def mostrar_notas(request):
    notas = Alumno_Curso_Prueba.objects.all()
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


class NotaCreateView(CreateView):
    model = Alumno_Curso_Prueba
    fields = ('prueba', 'nota', "alumno_curso")
    template_name = "notas/agregarnota.html"
    success_url = reverse_lazy('notas')


class NotaUpdateView(UpdateView):
    model = Alumno_Curso_Prueba
    fields = ('prueba', 'nota')
    success_url = reverse_lazy('notas')
    template_name = "notas/agregarnota.html"


class NotaDelete(DeleteView):
    model = Alumno_Curso_Prueba
    template_name = "notas/eliminarnota.html"
    context_object_name = "nota"
    success_url = reverse_lazy("notas")


# Vistas Cursos


def mostrar_cursos(request):
    cursos = Curso.objects.all().order_by("nombre_curso")
    context = {"cursos": cursos}
    return render(request, 'cursos/cursos.html', context)


class CursoCreateView(CreateView):
    model = Curso
    fields = ('nombre_curso', 'profesor')
    template_name = "cursos/agregarcurso.html"
    success_url = reverse_lazy('cursos')


class CursoUpdateView(UpdateView):
    model = Curso
    fields = ('nombre_curso', 'profesor')
    success_url = reverse_lazy('cursos')
    template_name = "cursos/agregarcurso.html"


class CursoDelete(DeleteView):
    model = Curso
    template_name = "cursos/eliminarcurso.html"
    context_object_name = "curso"
    success_url = reverse_lazy("cursos")

# Vista Pruebas


def mostrar_pruebas(request):
    pruebas = Prueba.objects.all().order_by("nombre_prueba")
    context = {"pruebas": pruebas}
    return render(request, 'pruebas/pruebas.html', context)


class PruebaCreateView(CreateView):
    model = Prueba
    fields = ('nombre_prueba', 'curso')
    template_name = "pruebas/agregarprueba.html"
    success_url = reverse_lazy('pruebas')


class PruebaUpdateView(UpdateView):
    model = Prueba
    fields = ('nombre_prueba', 'curso')
    success_url = reverse_lazy('pruebas')
    template_name = "pruebas/agregarprueba.html"


class PruebaDelete(DeleteView):
    model = Prueba
    template_name = "pruebas/eliminarprueba.html"
    context_object_name = "prueba"
    success_url = reverse_lazy("pruebas")


# Vista Agenda

def agenda(request):
    return render(request, 'agenda/agenda.html')
