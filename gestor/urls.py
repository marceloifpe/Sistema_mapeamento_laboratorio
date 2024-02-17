from django.urls import path
from . import views
from .views import calendario_reservas
from .views import calendario_reservas_materiais
from .views import teste
from .views import SalaListView, SalaCreateView, SalaUpdateView, SalaDetailView, SalaDeleteView



app_name = 'gestor'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('gestor_ver_salas/', views.gestor_ver_salas, name='gestor_ver_salas'),
    path('gestor_ver_materiais/', views.gestor_ver_materiais, name='gestor_ver_materiais'),
    path('calendario_reservas/', calendario_reservas, name='calendario_reservas'),
    path('calendario_reservas_materiais/', calendario_reservas_materiais, name='calendario_reservas_materiais'),
    path('teste/', teste, name='teste'),
    path('salas/', SalaListView.as_view(), name='sala_list'),
    path('salas/nova/', SalaCreateView.as_view(), name='sala_create'),
    path('salas/<int:pk>/editar/', SalaUpdateView.as_view(), name='sala_edit'),
    path('salas/<int:pk>/detail/', SalaDetailView.as_view(), name='sala_detail'),
    path('salas/<int:pk>/excluir/', SalaDeleteView.as_view(), name='sala_delete')
]