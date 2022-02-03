from django.urls import path
from . import views

urlpatterns = [
    path("alumnos", views.mostrar_alumnos, name="alumnos"),
    path("cursos/", views.mostrar_cursos, name="cursos"),
    path("pruebas/", views.mostrar_pruebas, name="pruebas"),
    path("notas/", views.mostrar_notas, name="product-detail"),
]
