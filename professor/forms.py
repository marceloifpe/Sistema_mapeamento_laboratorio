
# from django import forms
# from django.core.exceptions import ValidationError
# from django.utils import timezone
# from salas.models import Salas, Reservas
# from usuarios.models import Usuario
# import datetime

# class RealizarReservas(forms.ModelForm):
#     class Meta:
#         model = Reservas
#         fields = "__all__"
#         widgets = {
#             'data_reserva': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
#             'data_devolucao': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
#             'data_solicitacao': forms.HiddenInput(),  # Isso ocultará o campo no formulário
#         }

#     def __init__(self, *args, **kwargs):
#         super(). __init__(*args, **kwargs)
#         self.fields['usuarios'].widget = forms.HiddenInput()

#     def clean_data_reserva(self):
#         data_reserva = self.cleaned_data['data_reserva']
#         if data_reserva < datetime.date.today():
#             raise ValidationError('A data de reserva não pode ser no passado.')
#         return data_reserva

#     def clean_data_devolucao(self):
#         data_devolucao = self.cleaned_data['data_devolucao']
#         if data_devolucao < datetime.date.today():
#             raise ValidationError('A data de devolução não pode ser no passado.')
#         return data_devolucao

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from salas.models import Salas, Reservas
from materiais.models import Materiais, Reserva
from usuarios.models import Usuario
import datetime

class RealizarReservas(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = "__all__"
        widgets = {
            'data_reserva': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'data_devolucao': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'data_solicitacao': forms.HiddenInput(),  # Isso ocultará o campo no formulário
        }

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        self.fields['usuarios'].widget = forms.HiddenInput()
        self.fields['data_reserva'].label = 'Data de Reserva'
        self.fields['data_devolucao'].label = 'Data de Devolução'
        # Defina os rótulos para outros campos conforme necessário

    def clean_data_reserva(self):
        data_reserva = self.cleaned_data['data_reserva']
        if data_reserva < datetime.date.today():
            raise ValidationError('A data de reserva não pode ser no passado.')
        return data_reserva

    def clean_data_devolucao(self):
        data_devolucao = self.cleaned_data['data_devolucao']
        if data_devolucao < datetime.date.today():
            raise ValidationError('A data de devolução não pode ser no passado.')
        return data_devolucao
