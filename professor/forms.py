from django import forms

from salas.models import Salas, Reservas
from materiais.models import Materiais, Reserva
from usuarios.models import Usuario
from .validators import validate_date_not_past
from django.utils import timezone



class RealizarReservas(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = "__all__"
        widgets = {
            'data_reserva': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'data_devolucao': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'data_solicitacao': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        self.fields['usuarios'].widget = forms.HiddenInput()
        # Adicione a validação para os campos de data
        self.fields['data_reserva'].validators.append(validate_date_not_past)
        self.fields['data_devolucao'].validators.append(validate_date_not_past)

class RealizarReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = "__all__"
        widgets = {
            'data_reserva': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'data_devolucao': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'data_solicitacao': forms.HiddenInput(),
        }
    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        self.fields['usuarios'].widget = forms.HiddenInput()
        self.fields['data_reserva'].validators.append(validate_date_not_past)
        self.fields['data_devolucao'].validators.append(validate_date_not_past)

