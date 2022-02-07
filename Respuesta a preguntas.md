# Modelado de datos

_Nota: La query de creacion de tablas fue realizada en MySQL manualmente. Las Querys de las preguntas fueron realizadas en PostgreeSQL sobre la base de datos del proyecto, y basado en los nombres de tabla generados por Django con el modulo models. Lo menciono para que se entienda la diferencia en el nombre de tablas y/o algunos campos (como id) entre querys de creacion y querys de consultas._

_Foto del Modelado:_

![ModeladoCapitaria2](https://user-images.githubusercontent.com/52224826/152753561-4e6139bc-a73b-44c7-ae2b-83e409eb9e1d.jpg)

```
CREATE DATABASE colegio;
USE colegio;

CREATE TABLE IF NOT EXISTS alumno (
id_alumno INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(70) NOT NULL,
apellido VARCHAR(70) NOT NULL,
email VARCHAR(200) NOT NULL,
telefono VARCHAR(35),
);

CREATE TABLE IF NOT EXISTS profesor (
id_profesor INT UNSIGNED NOT NULL AUTO_INCREMENT,
nombre VARCHAR(70) NOT NULL,
apellido VARCHAR(70) NOT NULL,
email VARCHAR(200) NOT NULL,
telefono VARCHAR(35),
PRIMARY KEY (id_profesor)
);

CREATE TABLE IF NOT EXISTS curso (
id_curso INT UNSIGNED NOT NULL AUTO_INCREMENT,
nombre_curso VARCHAR(100) NOT NULL,
id_profesor INT UNSIGNED NOT NULL,
PRIMARY KEY (id_curso),
FOREIGN KEY (id_profesor) REFERENCES profesor (id_profesor)
ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS alumno_curso (
id_alumno_curso INT UNSIGNED NOT NULL AUTO_INCREMENT,
id_alumno INT UNSIGNED NOT NULL,
id_curso INT UNSIGNED NOT NULL,
PRIMARY KEY (id_alumno_curso),
FOREIGN KEY (id_alumno) REFERENCES alumno (id_alumno)
ON DELETE NO ACTION ON UPDATE NO ACTION,
FOREIGN KEY (id_curso) REFERENCES curso (id_curso)
ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS prueba (
id_prueba INT UNSIGNED NOT NULL AUTO_INCREMENT,
nombre_prueba VARCHAR(50) NOT NULL,
id_curso INT UNSIGNED NOT NULL,
PRIMARY KEY (id_prueba),
FOREIGN KEY (id_curso) REFERENCES curso (id_curso)
ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS alumno_curso_prueba (
id_alumno_curso_prueba INT UNSIGNED NOT NULL AUTO_INCREMENT,
nota FLOAT,
id_alumno_curso INT UNSIGNED NOT NULL,
id_prueba INT UNSIGNED NOT NULL,
PRIMARY KEY (id_alumno_curso_prueba),
FOREIGN KEY (id_alumno_curso) REFERENCES alumno_curso (id_alumno_curso)
ON DELETE NO ACTION ON UPDATE NO ACTION,
FOREIGN KEY (id_prueba) REFERENCES prueba (id_prueba)
ON DELETE NO ACTION ON UPDATE NO ACTION
);
```

P1=

```
SELECT CONCAT(nombre,' ', apellido) AS "Nombre Alumno", telefono, email
FROM core_alumno
INNER JOIN core_alumno_curso ON core_alumno.id=core_alumno_curso.alumno_id
INNER JOIN core_curso ON core_curso.id=core_alumno_curso.curso_id
WHERE nombre_curso='programacion';

```
![image](https://user-images.githubusercontent.com/52224826/152755434-fb0e01d6-91ec-4851-a897-30149a5053de.png)


P2=

```
SELECT nombre as "Nombre", nombre_curso as "Curso", ROUND(AVG(nota)::numeric, 1) as "Promedio"
FROM core_alumno
INNER JOIN core_alumno_curso ON core_alumno.id=core_alumno_curso.alumno_id
INNER JOIN core_curso ON core_curso.id=core_alumno_curso.curso_id
INNER JOIN core_alumno_curso_prueba ON core_alumno_curso.id=core_alumno_curso_prueba.alumno_curso_id
WHERE core_alumno.id=2 and nombre_curso='programacion'
GROUP BY nombre, nombre_curso;
```
![image](https://user-images.githubusercontent.com/52224826/152755825-63588e9b-d8bf-436c-b0bc-e3e2958cf1c4.png)

P3=

```
SELECT nombre as "Nombre", nombre_curso as "Curso", ROUND(AVG(nota)::numeric, 1) as "Promedio"
FROM core_alumno
INNER JOIN core_alumno_curso ON core_alumno.id=core_alumno_curso.alumno_id
INNER JOIN core_curso ON core_curso.id=core_alumno_curso.curso_id
INNER JOIN core_alumno_curso_prueba ON core_alumno_curso.id=core_alumno_curso_prueba.alumno_curso_id
GROUP BY nombre, nombre_curso;
```
![image](https://user-images.githubusercontent.com/52224826/152756006-14e2d9de-29b4-44ce-b7a6-a04055e0365f.png)

P4=

```
SELECT nombre as "Nombre", nombre_curso as "Curso", ROUND(AVG(nota)::numeric, 1) as "Promedio"
FROM core_alumno
INNER JOIN core_alumno_curso ON core_alumno.id=core_alumno_curso.alumno_id
INNER JOIN core_curso ON core_curso.id=core_alumno_curso.curso_id
INNER JOIN core_alumno_curso_prueba ON core_alumno_curso.id=core_alumno_curso_prueba.alumno_curso_id
WHERE nota<4 GROUP BY nombre, nombre_curso HAVING COUNT(nombre)>1;
```
![image](https://user-images.githubusercontent.com/52224826/152756174-4158fd88-e1bf-4895-b8af-3fbd279e74fd.png)

P5=

```
B)190... Esto se debe ya que al hacer consultas multitablas sin join se obtienen productos cartesianos. Sin el where, serian 400 registros, pero con el where se reducen a 19 registros para el de mejor posicion, 18 para el siguiente, y asi sucesivamente dandose el patron de (n-1)x(n/2)= 190.
```

# Diseño de software

# Backend

P1.- CRUD alumnos, cursos, pruebas y notas.

All the views of the crud are on the views.py file.

- [Views](https://github.com/MarceloDeLaBarrera/test-capitaria/blob/develop/core/views.py)

_Some views render on templates:_
![image](https://user-images.githubusercontent.com/52224826/152756588-57078f0e-2e09-4255-a737-f7432ade5dc1.png)
![image](https://user-images.githubusercontent.com/52224826/152756666-25933ea8-881d-4f77-ae6c-bf32bbaf007e.png)



P2.- Listar a los alumnos junto a su promedio de notas.

![image](https://user-images.githubusercontent.com/52224826/152754399-f314a128-5642-44ca-be79-d371f7213e3f.png)
![image](https://user-images.githubusercontent.com/52224826/152769842-49390b18-9865-408b-84cb-7bd235d71787.png)
![image](https://user-images.githubusercontent.com/52224826/152754168-12d57bff-3021-4e54-b652-fdbe3b162c53.png)




P3.- Filtar a todos los alumnos con más de un ramo con promedio rojo.

![image](https://user-images.githubusercontent.com/52224826/152754467-c9b8a1bb-e18d-4bc2-860f-d152700bbe03.png)
![image](https://user-images.githubusercontent.com/52224826/152754044-45ffb2ae-9670-4c97-be48-6157fbf06471.png)

# Frontend

The files releated to calendar are app.js, agenda.html, and styles.css.

- [Agenda.html](https://github.com/MarceloDeLaBarrera/test-capitaria/blob/develop/core/Template/agenda/agenda.html)
- [Agenda JS](https://github.com/MarceloDeLaBarrera/test-capitaria/blob/develop/static/js/app.js)
- [Styles](https://github.com/MarceloDeLaBarrera/test-capitaria/blob/develop/static/css/styles.css)

![image](https://user-images.githubusercontent.com/52224826/152754599-a2800d2c-7ed1-4815-a202-ecba038033eb.png)
