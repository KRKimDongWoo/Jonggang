from todos.models import Todo
from rest_framework import serializers 

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ('date', 'memo', 'course', 'professor', 'todo_type', 'done')
