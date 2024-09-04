from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ('id_nutricionista', 'dia','horario', 'tem_patologia')

    # data = models.DateField()
    # horario = models.TimeField()
    # status = models.CharField(max_length=20, choices=[
    #     ('Pendente', 'Pendente'),
    #     ('Confirmado', 'Confirmado'),
    #     ('Cancelado', 'Cancelado')
    # ])
    # tem_patologia = models.BooleanField()