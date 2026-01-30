from django.urls import path
from . import views

urlpatterns = [
    path('', views.memory_wall, name='memory_wall'),
    path('add/', views.add_memory, name='add_memory'),
]
