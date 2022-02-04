from django.db import models

# Create your models here.


class Alumno(models.Model):
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    email = models.EmailField(max_length=200, null=True)
    telefono = models.CharField(max_length=35, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['id']


class Profesor(models.Model):
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    email = models.EmailField(max_length=200, null=True)
    telefono = models.CharField(max_length=35, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['id']

    class Meta:
        ordering = ['id']


class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100, null=True)
    profesor = models.ForeignKey(
        Profesor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre_curso

    class Meta:
        ordering = ['id']


class Alumno_Curso(models.Model):
    alumno = models.ForeignKey(
        Alumno, on_delete=models.SET_NULL, null=True)
    curso = models.ForeignKey(
        Curso, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id']

    @property
    def nombre_curso(self):
        return self.curso.nombre_curso

    @property
    def nombre_alumno(self):
        return self.alumno.nombre


class Prueba(models.Model):
    nombre_prueba = models.CharField(max_length=60)
    curso = models.ForeignKey(
        Curso, on_delete=models.SET_NULL, null=True)

    @property
    def nombre_curso(self):
        return self.curso.nombre_curso

    class Meta:
        ordering = ['id']


class Alumno_Curso_Prueba(models.Model):
    alumno_curso = models.ForeignKey(
        Alumno_Curso, on_delete=models.SET_NULL, null=True)
    prueba = models.ForeignKey(
        Prueba, on_delete=models.SET_NULL, null=True)
    nota = models.FloatField(blank=True, null=True)

    def __str__(self):
        # return f"ID: {str(self.id)} - Alumno: {self.alumno_curso.alumno.nombre} - Prueba: {self.prueba.nombre_prueba} - Nota: {str(self.nota)}"
        return f"{str(self.nota)} {self.alumno_curso.alumno.nombre}"

    @property
    def nombre_prueba(self):
        return self.prueba.nombre_prueba

    @property
    def nombre_alumno(self):
        return self.alumno_curso.alumno.nombre

    @property
    def nombre_curso(self):
        return self.alumno_curso.curso.nombre_curso

    class Meta:
        ordering = ['id']
