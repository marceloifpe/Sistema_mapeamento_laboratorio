from django.urls import path
from . import views

urlpatterns = [
    path('homee/', views.homee, name='homee'),
    path('ver_salas_professor/<int:id>', views.ver_salas_professor, name='ver_salas_professor')
    
]
