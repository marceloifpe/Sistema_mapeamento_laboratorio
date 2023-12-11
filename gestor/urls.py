from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('gestor_ver_salas/', views.gestor_ver_salas, name='gestor_ver_salas'),
    path('gestor_ver_materiais/', views.gestor_ver_materiais, name='gestor_ver_materiais')
]   
