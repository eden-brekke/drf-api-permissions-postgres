# Lab 32

## Django REST Framework Permissions and PostgreSQL

### Author

- Eden Brekke
- Followed the class demo and altered to what I wanted

### Collaborator

Worked with Benjamin Carter

### How to Run this Application

- python -m venv .venv
- .\.venv\Scripts\activate
- pip install django
- pip install djangorestframework
- django-admin startproject projectname
- python manage.py migrate
- python manage.py runserver
- python manage.py startapp app
- Make TUV and add to settings
- python manage.py makemigrations app
- python manage.py createsuperuser
- python manage.py runserver

- docker compose up --build
- docker compose run web bash
- Redo python manage stuff in docker terminal!

### Tests

- to run tests import the class PetPic
- import django.test import APITestCase
- python manage.py test to run tests

- I referenced the tests provided in today's demo

### Overview

- This was fun, incorporating a new database and permissions. 