from django.urls import path
from . import views
from .views import calendario_reservas

app_name = 'gestor'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('gestor_ver_salas/', views.gestor_ver_salas, name='gestor_ver_salas'),
    path('gestor_ver_materiais/', views.gestor_ver_materiais, name='gestor_ver_materiais'),
    path('calendario_reservas/', calendario_reservas, name='calendario_reservas')
]   
