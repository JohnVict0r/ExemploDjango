from django.db import models

# Create your models here.

class TodoItem(models.Model):
    name = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name