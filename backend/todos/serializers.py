from todos.models import Todo
from rest_framework import serializers 

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'date', 'memo', 'course', 'professor', 'todo_type', 'done')
