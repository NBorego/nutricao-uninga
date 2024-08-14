from django import forms
from .models import Alimento

class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = ('nome', 'imagem','descricao', 'calorias', 'proteinas', 'sodio')