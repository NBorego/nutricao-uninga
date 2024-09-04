from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Agendamento
from login.models import Nutricionista
from datetime import date

class AgendamentoForm(forms.ModelForm):
    nutricionista = forms.ModelChoiceField(
        queryset=Nutricionista.objects.all(),
        label="Nutricionista",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    dia = forms.DateField(
        label=_("Dia"),
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'min': date.today().strftime('%Y-%m-%d')
        }),
    )

    horario = forms.TimeField(
        label="Horário",
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'type': 'time'
        }),
    )

    tem_patologia = forms.BooleanField(
        label="Possui Patologia?",
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input d-block',
            'style': 'width: 1.3rem; height: 1.3rem;'
        }),
    )

    class Meta:
        model = Agendamento
        fields = ('nutricionista', 'dia','horario', 'tem_patologia')