from django import forms

from salas.models import Salas, Reservas
from usuarios.models import Usuario

class RealizarReservas(forms.ModelForm):
    class Meta:
        model = Reservas
        # fields = ('salas','data_reserva','data_devolucao','data_solicitacao')
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        self.fields['usuarios'].widget = forms.HiddenInput()