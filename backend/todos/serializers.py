from todos.models import Todo, Course
from rest_framework import serializers 

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 
                  'date', 
                  'memo', 
                  'course', 
                  'professor', 
                  'todo_type', 
                  'done')

class CourseSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_id', 
                  'course_num', 
                  'professor', 
                  'course_name', 
                  'grade_point',
                  'time')

class CourseRecommendSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())

    class Meta:
        model = Course
        fields = ('todos')
