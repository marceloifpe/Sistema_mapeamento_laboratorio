from django.db import models
from datetime import date
from usuarios.models import Usuario

class Materiais(models.Model):
    nome_do_material = models.CharField(max_length=30)
    reservado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Material'

    def __str__(self):
        return self.nome_do_material

class Reserva(models.Model):
    usuarios = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    data_reserva = models.DateTimeField()
    data_devolucao = models.DateTimeField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    materiais = models.ForeignKey(Materiais, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = 'Reserva'
    
    def __str__(self) -> str:
        return f"{self.usuarios} | {self.materiais}"
