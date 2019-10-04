from django.urls import path, include
from rest_framework import routers

from .views import TodoViewSet, CourseView

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet, base_name='todos')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/course/', CourseView.as_view()),
]

