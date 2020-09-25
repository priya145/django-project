# django-project
A responsive web app built with Django 3.0.5.
***
## Requirements
- Django = 3.0.5
- python = 3.7.3
- djangorestframework = 3.11.0
***
## INSTALLED_APPS
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'rest_framework',
]
```
***
## urls.py in mysite
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
```
***
## urls.py in myapp
```
urlpatterns = [

path('', user_views.mainhome, name="mainhome"),
path('base_view', user_views.base, name="base"),
url(r'^business_api/',user_views.business_api.as_view()),

]


```
***
## How to run it
- to migrate the database
```
$ cd mysite
$ python manage.py makemigrations
$ python manage.py migrate
```
- to run the program
```
python manage.py runserver
```
Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).Open the address in the browser
***
## Project Tree
```
├── mysite
    ├── myapp
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── migrations
    │   ├── tests.py
    │   ├── forms.py
    │   ├── urls.py
    │   ├── serializer.py
    │   └── views.py
    │
    ├── db.sqlite3
    ├── manage.py
    │
    ├── mysite
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    ├── static
    │   └── myapp
    │
    ├── templates
    │   ├── myapp
    │       ├── index.html
    │       ├── base.html
    │
    
 ```
