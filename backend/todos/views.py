from rest_framework import viewsets
from todos.serializers import TodoSerializer
from todos.models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Create your views here.
