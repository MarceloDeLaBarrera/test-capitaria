from django.contrib import admin
from core.models import Alumno, Alumno_Curso, Alumno_Curso_Prueba, Profesor, Prueba, Curso

# Register your models here.


class Alumno_Admin(admin.ModelAdmin):
    search_fields = ("nombre", "apellido")
    list_display = ("id", "nombre", "apellido")


class Profesor_Admin(admin.ModelAdmin):
    search_fields = ("nombre", "apellido")


class Prueba_Admin(admin.ModelAdmin):
    list_display = ("nombre_curso", "nombre_prueba")


class Alumno_Curso_Admin(admin.ModelAdmin):
    list_display = ("id", "nombre_curso", "nombre_alumno")


class Alumno_Curso_Prueba_Admin(admin.ModelAdmin):
    list_display = ("nombre_alumno", "nombre_curso", "nombre_prueba", "nota")
    list_filter = ("alumno_curso__alumno",)


admin.site.register(Alumno, Alumno_Admin)
admin.site.register(Profesor, Profesor_Admin)
admin.site.register(Alumno_Curso, Alumno_Curso_Admin)
admin.site.register(Alumno_Curso_Prueba, Alumno_Curso_Prueba_Admin)
admin.site.register(Curso)
admin.site.register(Prueba, Prueba_Admin)
