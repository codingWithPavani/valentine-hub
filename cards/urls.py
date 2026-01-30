from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_card, name='create_card'),
    path('view/<int:card_id>/', views.view_card, name='view_card'),
]
