from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions

from todos.serializers import TodoSerializer
from todos.models import Todo

from rest_framework.status import (
    HTTP_400_BAD_REQUEST
)

class login(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({"error", "Invalid Credentials"}, status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = TodoSerializer

    def get_queryset(self):
        return self.request.user.todos.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Create your views here.
