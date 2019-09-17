# Tutorial

## Intalando o Django

`$ pip install django`

## Criando o projeto

`$ django-admin startproject exemplodjango .`

## configuração inicial

`$ ./manage.py migrate

## Configurando usuário

`$ ./manage.py createsuperuser`

## Criando um novo App

`$ ./manage.py startapp todo`

é necessário instalar o app em settings.py

INSTALLED_APPS = [
    ...
    'todo'
]

`$ ./manage.py makemigrations`
`$ ./manage.py migrate`

## Rodando a aplicação

$ ./mange.py runserver`