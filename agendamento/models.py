from django.db import models
from login.models import Cliente, Nutricionista

class Agendamento(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_nutricionista = models.ForeignKey(Nutricionista, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    status = models.CharField(max_length=20, choices=[
        ('Pendente', 'Pendente'),
        ('Confirmado', 'Confirmado'),
        ('Cancelado', 'Cancelado')
    ])
    tem_patologia = models.BooleanField()

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"

