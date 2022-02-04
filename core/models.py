from django.db import models

# Create your models here.


class Alumno(models.Model):
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    email = models.EmailField(max_length=200, null=True)
    telefono = models.CharField(max_length=35, null=True)

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    email = models.EmailField(max_length=200, null=True)
    telefono = models.CharField(max_length=35, null=True)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100, null=True)
    profesor = models.ForeignKey(
        Profesor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre_curso


class Alumno_Curso(models.Model):
    alumno = models.ForeignKey(
        Alumno, on_delete=models.SET_NULL, null=True)
    curso = models.ForeignKey(
        Curso, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)


class Prueba(models.Model):
    nombre_prueba = models.CharField(max_length=60)
    curso = models.ForeignKey(
        Curso, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre_prueba


class Alumno_Curso_Prueba(models.Model):
    alumno_curso = models.ForeignKey(
        Alumno_Curso, on_delete=models.SET_NULL, null=True)
    prueba = models.ForeignKey(
        Prueba, on_delete=models.SET_NULL, null=True)
    nota = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"ID: {str(self.id)} - Alumno: {self.alumno_curso.alumno.nombre} - Prueba: {self.prueba.nombre_prueba} - Nota: {str(self.nota)}"
