from django.db import models
from datetime import date

from usuarios.models import Usuario


class Salas(models.Model):

    UABJ = 'UABJ'
    AEB = 'AEB'

    LOCAL_CHOICES = [
        (UABJ, 'UABJ'),
        (AEB, 'AEB'),
    ]
    nome_da_sala = models.CharField(max_length = 30)
    local = models.CharField(max_length = 4, choices = LOCAL_CHOICES, default = UABJ)
    reservado = models.BooleanField(default = False)
    quem_reservou = models.CharField(max_length = 30)
    data_reserva = models.DateTimeField()
    data_devolucao = models.DateTimeField()
    data_solicitacao = models.DateField(default = date.today)
    usuarios = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = 'Sala'

    def __str__(self):
        return self.nome_da_sala