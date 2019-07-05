from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    date = models.DateTimeField()
    memo = models.CharField(max_length=30, null=True)
    course = models.CharField(max_length=20)
    professor = models.CharField(max_length=20)
    todo_type = models.CharField(max_length=10)
    done = models.BooleanField()
    owner = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE, null=True)


# Create your models here.
