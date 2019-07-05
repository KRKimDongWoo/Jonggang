from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'todos', views.TodoViewSet, base_name='todos')

urlpatterns = [
#    url(r'^api/', include(router.urls)),
    path('', include('todos.urls')),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
