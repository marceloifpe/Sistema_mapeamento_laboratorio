# from django import forms

# from salas.models import Salas, Reservas
# from usuarios.models import Usuario

# class RealizarReservas(forms.ModelForm):
#     class Meta:
#         model = Reservas
#         # fields = ('salas','data_reserva','data_devolucao','data_solicitacao')
#         fields = "__all__"
#     def __init__(self, *args, **kwargs):
#         super(). __init__(*args, **kwargs)
#         self.fields['usuarios'].widget = forms.HiddenInput()

from django import forms
from salas.models import Salas, Reservas
from usuarios.models import Usuario

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
