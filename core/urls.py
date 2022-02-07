from django.urls import path

from . import views

urlpatterns = [
    path("alumnos/", views.mostrar_alumnos, name="alumnos"),
    path('agregaralumno/', views.agregar_alumno, name="agregar-alumno"),
    path('alumnos/eliminar-alumno/<int:id>/',
         views.eliminar_alumno, name="eliminaralumno"),
    path('alumnos/editar-alumno/<int:id>/',
         views.editar_alumno, name="editaralumno"),
    path('actualizar-alumno/', views.actualizar_alumno, name="actualizaralumno"),
]

urlpatterns_grade = [
    path("cursos/", views.mostrar_cursos, name="cursos"),
    path("cursos/agregarcurso/",
         views.CursoCreateView.as_view(), name="crear-curso"),
    path('cursos/editar-curso/<int:pk>/',
         views.CursoUpdateView.as_view(), name="editarcurso"),
    path('cursos/eliminar-curso/<int:pk>/',
         views.CursoDelete.as_view(), name="eliminarcurso"),

]

urlpatterns_tests = [
    path("pruebas/", views.mostrar_pruebas, name="pruebas"),
    path('agregarprueba',
         views.PruebaCreateView.as_view(), name="agregar-prueba"),
    path('pruebas/editar-prueba/<int:pk>/',
         views.CursoUpdateView.as_view(), name="editarprueba"),
    path('pruebas/eliminar-prueba/<int:pk>/',
         views.CursoDelete.as_view(), name="eliminarprueba"),
]

urlpatterns_scores = [
    path("notas/", views.mostrar_notas, name="notas"),
    path("listado-promedio-notas/", views.listar_promedionotas,
         name="listadopromedionotas"),
]

urlpatterns += urlpatterns_grade+urlpatterns_tests+urlpatterns_scores
