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

    nome_da_sala = models.CharField(max_length=30)
    local = models.CharField(max_length=4, choices=LOCAL_CHOICES, default=UABJ)
    reservado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Sala'

    def __str__(self):
        return f"{self.nome_da_sala} ({self.get_local_display()})"  # Retorna nome da sala e local formatados

class Reservas(models.Model):
    usuarios = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    data_reserva = models.DateTimeField()
    data_devolucao = models.DateTimeField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    salas = models.ForeignKey(Salas, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = 'Reserva'
    
    def __str__(self):
        return f"{self.usuarios} | {self.salas}"
