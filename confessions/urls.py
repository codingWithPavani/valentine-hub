from django.urls import path
from .views import wishes_wall

urlpatterns = [
    path('', wishes_wall, name='wishes_wall'),
]
