from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Agendamento
from login.models import Nutricionista, User
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

    horario = forms.ChoiceField(
        label="Horário",
        choices=Agendamento.HORARIO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
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

    def __init__(self, *args, **kwargs):
        self.cliente = kwargs.pop('cliente', None)  # Retira o cliente dos argumentos
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        agendamento = super().save(commit=False)
        agendamento.cliente = self.cliente  # Atribui o cliente atual
        if commit:
            agendamento.save()
        return agendamento
    
class FotoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('foto',)
        widgets = {
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }

class EditarAgendamentoForm(forms.ModelForm):
    dia = forms.DateField(
        label=_("Dia"),
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'min': date.today().strftime('%Y-%m-%d')
        }),
    )

    horario = forms.ChoiceField(
        label="Horário",
        choices=Agendamento.HORARIO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Agendamento
        fields = ('dia','horario')    