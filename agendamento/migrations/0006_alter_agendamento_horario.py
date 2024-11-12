# Generated by Django 5.1 on 2024-11-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0005_alter_agendamento_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='horario',
            field=models.CharField(choices=[('8:00', '8:00'), ('11:00', '11:00')], default='7:50 a 8:00', max_length=20),
        ),
    ]
