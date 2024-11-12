from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from login.models import Cliente, Nutricionista

class Agendamento(models.Model):
    HORARIO_CHOICES = [
        ('8:00', '8:00'),
        ('9:00', '9:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
    ]

    cliente = ForeignKey(Cliente, on_delete=models.CASCADE, related_name='agendamento', default=1)
    nutricionista = ForeignKey(Nutricionista, on_delete=models.CASCADE,  related_name='agendamento', default=1)
    dia = models.DateField()
    horario = models.CharField(max_length=20, choices=HORARIO_CHOICES, default='7:50 a 8:00')
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
