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
    
    
    class Meta:
        verbose_name = 'Sala'

    def __str__(self):
        return self.nome_da_sala

class Reservas(models.Model):
    usuarios = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    data_reserva = models.DateField()
    data_devolucao = models.DateField()
    data_solicitacao = models.DateField(default = date.today)
    salas = models.ForeignKey(Salas, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = 'Reserva'
    
    def __str__(self) -> str:
        return f"{self.usuarios} | {self.salas}"
    

    