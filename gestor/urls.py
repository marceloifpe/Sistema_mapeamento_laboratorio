from django.urls import path
from . import views
from .views import calendario_reservas

urlpatterns = [
    path('home/', views.home, name='home'),
    path('gestor_ver_salas/', views.gestor_ver_salas, name='gestor_ver_salas'),
    path('calendario_reservas/', calendario_reservas, name='calendario_reservas')
]   
