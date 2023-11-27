from django.urls import path
from . import views

urlpatterns = [
    path('homee/', views.homee, name='homee'),
    path('ver_salas/<int:id>', views.ver_salas, name='ver_salas')
    
]