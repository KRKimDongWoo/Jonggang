from django.urls import path, include
from rest_framework import routers

from .views import TodoViewSet

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet, base_name='todos')

urlpatterns = [
    path('api/', include(router.urls)),
]

