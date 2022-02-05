Modelado de datos

CREATE DATABASE colegio;
USE colegio;

CREATE TABLE IF NOT EXISTS alumno (
id_alumno INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
apellido VARCHAR(50) NOT NULL,
email VARCHAR(80) NOT NULL,
telefono VARCHAR(30),
);

CREATE TABLE IF NOT EXISTS profesor (
id_profesor INT UNSIGNED NOT NULL AUTO_INCREMENT,
nombre VARCHAR(50) NOT NULL,
apellido VARCHAR(50) NOT NULL,
email VARCHAR(80) NOT NULL,
telefono VARCHAR(30),
PRIMARY KEY (id_profesor)
);

CREATE TABLE IF NOT EXISTS curso (
id_curso INT UNSIGNED NOT NULL AUTO_INCREMENT,
nombre_curso VARCHAR(50) NOT NULL,
id_profesor INT UNSIGNED NOT NULL,
PRIMARY KEY (id_curso),
FOREIGN KEY (id_profesor) REFERENCES profesor (id_profesor)
ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS alumno_curso (
id_alumno_curso INT UNSIGNED NOT NULL AUTO_INCREMENT,
id_alumno INT UNSIGNED NOT NULL,
PRIMARY KEY (id_alumno_curso),
FOREIGN KEY (id_alumno) REFERENCES alumno (id_alumno)
ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS prueba (
id_prueba INT UNSIGNED NOT NULL AUTO_INCREMENT,
nombre_prueba VARCHAR(50) NOT NULL,
PRIMARY KEY (id_prueba)
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

P1=

SELECT nombre, nombre_curso
FROM core_alumno
INNER JOIN core_alumno_curso ON core_alumno.id=core_alumno_curso.alumno_id
INNER JOIN core_curso ON core_curso.id=core_alumno_curso.curso_id
WHERE nombre_curso='programacion';

P2=

SELECT nombre, nombre_curso, ROUND(AVG(nota)::numeric, 1)
FROM core_alumno
INNER JOIN core_alumno_curso ON core_alumno.id=core_alumno_curso.alumno_id
INNER JOIN core_curso ON core_curso.id=core_alumno_curso.curso_id
INNER JOIN core_alumno_curso_prueba ON core_alumno_curso.id=core_alumno_curso_prueba.alumno_curso_id
WHERE core_alumno.id=1 and nombre_curso='programación'
GROUP BY nombre, nombre_curso;

P3=

SELECT nombre, nombre_curso, ROUND(AVG(nota)::numeric, 1)
FROM core_alumno
INNER JOIN core_alumno_curso ON core_alumno.id=core_alumno_curso.alumno_id
INNER JOIN core_curso ON core_curso.id=core_alumno_curso.curso_id
INNER JOIN core_alumno_curso_prueba ON core_alumno_curso.id=core_alumno_curso_prueba.alumno_curso_id
GROUP BY nombre, nombre_curso;

P4=

SELECT nombre, nombre_curso, AVG(nota)
FROM core_alumno
INNER JOIN core_alumno_curso ON core_alumno.id=core_alumno_curso.alumno_id
INNER JOIN core_curso ON core_curso.id=core_alumno_curso.curso_id
INNER JOIN core_alumno_curso_prueba ON core_alumno_curso.id=core_alumno_curso_prueba.alumno_curso_id
WHERE nota<4 GROUP BY nombre, nombre_curso HAVING COUNT(nombre)>1;

P5= B) 190... Esto se debe ya que al hacer consultas multitablas sin join se obtienen productos cartesianos. Sin el where, serian 400 registros, pero con el where se reducen a 19 registros para el de mejor posicion, 18 para el siguiente, y asi sucesivamente (n-1)\*(n/2)= 190.
