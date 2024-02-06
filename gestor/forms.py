from django import forms
from .models import Salas

class SalaForm(forms.ModelForm):
    class Meta:
        model = Salas
        fields = ['nome_da_sala', 'local']  