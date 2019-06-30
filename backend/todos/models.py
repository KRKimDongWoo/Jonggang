from django.db import models

class Todo(models.Model):
    date = models.DateTimeField()
    memo = models.CharField(max_length=30)
    course = models.CharField(max_length=20)
    professor = models.CharField(max_length=20)
    todo_type = models.CharField(max_length=10)
    done = models.BooleanField()

# Create your models here.
