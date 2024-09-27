pip install virtualenv

// TODO verificar proceso de activacion

```
$ virtualenvn venv
```

source venv/bin/activate

> django --version
> zsh: command not found: django
> django-admin --version
> 5.1.1

> django-admin startproject mysite .
> ~/Workspaces/django-project

> python manage.py runserver <port>

# References:

https://www.youtube.com/watch?v=T1intZyhXDU&ab_channel=Fazt

# Crear aplicaciones

> python manage.py starapp blog

# migraciones

Default database django's structure

> python manage.py makemigrations
> python manage.py migrate

Especify project myapp

> python manage.py migrate myapp

# create models

myapp/models.py needs some changes

# store data

> python manage.py shell

> > > from myapp.models import Project, Task
> > > p = Project(name='aplicacion movil')
> > > p
> > > <Project: Project object (None)>
> > > p.save()

# creat task project

> > > p=Project.objects.get(id=1)
> > > p
> > > <Project: Project object (1)>
> > > p.task_set.all()
> > > <QuerySet []>
> > > p.task_set.create(title="descargar id")
> > > <Task: Task object (1)>

# Create super user

> python manage.py createsuperuser
> Username (leave blank to use 'eddy'): admin
> Email address: edison@cladian.com
> Password:
> Password (again):
> This password is too common.
> This password is entirely numeric.
> Bypass password validation and create user anyway? [y/N]: y
> Superuser created successfully.
> python manage.py runserver
> Watching for file changes with StatReloader
> Performing system checks...

login and access
http://127.0.0.1:8000/admin
