from django.contrib import admin

# Register your models here.
from todo.models import TodoItem

admin.site.register(TodoItem)