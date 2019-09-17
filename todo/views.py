from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from todo.models import TodoItem
from todo.serializers import TodoItemSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    queryset = TodoItem.objects.all()
