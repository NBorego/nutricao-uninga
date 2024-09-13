from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Alimento

class AlimentoForm(forms.ModelForm):
    quantidade_gml = forms.FloatField(label='Quantidade (g/ml)')

    class Meta:
        model = Alimento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})