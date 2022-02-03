from django.contrib import admin
from core.models import Alumno, Alumno_Curso, Alumno_Curso_Prueba, Profesor, Prueba, Curso

# Register your models here.


class Alumno_Admin(admin.ModelAdmin):
    search_fields = ("nombre", "apellido")


class Profesor_Admin(admin.ModelAdmin):
    search_fields = ("nombre", "apellido")


admin.site.register(Alumno, Alumno_Admin)
admin.site.register(Profesor, Profesor_Admin)
admin.site.register(Alumno_Curso)
admin.site.register(Alumno_Curso_Prueba)
admin.site.register(Curso)
admin.site.register(Prueba)
