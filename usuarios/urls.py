from django.urls import path
from . import views

urlpatterns = [
    # Define uma rota para a view 'login'
    path('login/', views.login, name='login'),
    
    # Define uma rota para a view 'cadastro'
    path('cadastro/', views.cadastro, name='cadastro'),
    
    # Define uma rota para a view 'valida_cadastro'
    path('valida_cadastro/', views.valida_cadastro, name='valida_cadastro'),
    
    # Define uma rota para a view 'valida_login'
    path('valida_login/', views.valida_login, name='valida_login'),

    path('sair/', views.sair, name='sair'),
    

    
]
