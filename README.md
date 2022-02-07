# Capitaria Test

_This is a Crud Project, a school management system, where you can create, edit, delete and update courses, students, scores and test. Also, you could see the average scores of each student of each course, and filter the ones that are failing. Also, has the prototype of a hour reservation system._

## Table of contents

- [Starting](#starting-)
- [Requeriments](#requeriments-)
- [Install and Run the project](#Install-and-Run-the-project-)
- [Built in](#built-in-%EF%B8%8F)
- [Answers of Questions](#answers-of-questions-)
- [Autor](#autor-%EF%B8%8F)

## Starting 🚀

_Fork the project to your profile, and then clone to your local machine._

```
git clone <repo-link>
git add .
git commit -m <"message">
git push origin master
```

## Requeriments 📋

_This project uses python 3.9.5, don't tested yet on other versions of python._
_Also, you need to have installed Postgresql to make database connection._

_To install all dependencies necessary to run the project on your local development environment you need to use pip to install requeriments.txt_

```
pip install -r .\requirements.txt
```

## Install and Run the project 🔧

_1.- Create your own database file. I use PostgreSQL on this case._

_2.- To run the project, you have to create your own .env file to hidden your secret keys and DateBase connection._

_Note 1: Put debug=1 on local, or 0 on production._

```
SECRET_KEY= <yoursecretkey>
DEBUG_ENV=1

DATABASE_NAME= <yourdatabase_name>
USER= <youruser>
PASSWORD= <yourpassword>
HOST= 127.0.0.1
DATABASE_PORT= 5432
```

_Note2: You can create aleatory secret keys with the following command:_

```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

_3.- Make mirgations and migrate the model to database._

```
python manage.py makemigrations
python manage.py migrate
```

_4.- You can create your own superuser to access Django Admin Panel_

```
python manage.py createsuperuser
```

_5.- To fill the database with the data used on this project for test, you can run THIS on the Project Directory:_

```
python manage.py loaddata .\core\fixtures\database.json

Note: Also, if the last one doesn't works, you can try: " python manage.py loaddata " or " python manage.py loaddata database.json " should be find the file, because django search on fixtures directories.
```

_6. Finally, run server on your local machine._

```
python manage.py runserver
```

## Built in 🛠️

- [Django](http://www.djangoproject.com/)
- [Python](https://www.python.org/)
- [HTML](https://)
- [CSS](http://)

## Answers of Questions ⭐

[Answers](https://github.com/MarceloDeLaBarrera/test-capitaria/blob/develop/Respuesta%20a%20preguntas.md)

## Autor ✒️

- **Marcelo De La Barrera** - [marcelodelabarrera](https://github.com/marcelodelabarrera)
