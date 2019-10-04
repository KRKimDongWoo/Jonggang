from django.db import models
from django.contrib.auth.models import User

class ShortenName(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_type = models.CharField(max_length=8)
    university = models.CharField(max_length=16)
    department = models.CharField(max_length=32)
    degree = models.CharField(max_length=16)
    grade = models.CharField(max_length=8)
    course_name = models.CharField(max_length=32)
    course_id = models.CharField(max_length=16)
    course_num = models.CharField(max_length=16)
    course_subname = models.CharField(max_length=32)
    grade_point = models.IntegerField()
    length_course = models.IntegerField()
    length_lab = models.IntegerField()
    time = models.CharField(max_length=32)
    course_content = models.CharField(max_length=32)
    classroom = models.CharField(max_length=16)
    professor = models.CharField(max_length=32)
    max_student = models.CharField(max_length=8)
    current_student = models.IntegerField()
    etc = models.CharField(max_length=128)
    language = models.CharField(max_length=8)
    course_altname = models.ManyToManyField(ShortenName, blank=True)

    def __str__(self):
        return self.course_name + ": " + self.course_id + "-" + self.course_num

class Todo(models.Model):
    date = models.DateTimeField()
    memo = models.CharField(max_length=30, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    todo_type = models.CharField(max_length=10)
    done = models.BooleanField()
    owner = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.course.course_name + todo_type

# Create your models here.
