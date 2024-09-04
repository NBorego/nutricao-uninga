from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from login.models import Cliente, Nutricionista

class Agendamento(models.Model):
    cliente = ForeignKey(Cliente, on_delete=models.CASCADE, related_name='agendamento', default=1)
    nutricionista = ForeignKey(Nutricionista, on_delete=models.CASCADE,  related_name='agendamento', default=1)
    dia = models.DateField()
    horario = models.TimeField()
    status = models.CharField(max_length=20, choices=[
        ('Pendente', 'Pendente'),
        ('Confirmado', 'Confirmado'),
        ('Cancelado', 'Cancelado')
        ], 
        default='Pendente',
    )
    tem_patologia = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
