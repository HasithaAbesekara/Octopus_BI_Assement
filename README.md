
Install Django and other required packages:
  pip install django pandas

## Pre-Requisites
pip install django
pip install psycopg2

## Commands to create project and app
django-admin startproject <project name>
python manage.py startapp <REST API>

## DB connections
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'restfulapiDB',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost'
    }
}

## Model creation steps
python manage.py makemigrations <API APP name>
python manage.py migrate

## Run App API
python manage.py runserver