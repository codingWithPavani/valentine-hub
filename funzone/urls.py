from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun_home, name='funzone'),
    path('love-calculator/', views.love_calculator, name='love_calculator'),
    path('message-generator/', views.message_generator, name='message_generator'),
    path('game/', views.heart_game, name='heart_game'),
]
