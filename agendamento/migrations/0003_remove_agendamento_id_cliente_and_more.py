# Generated by Django 5.1 on 2024-09-04 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0002_alter_agendamento_tem_patologia'),
        ('login', '0026_alter_user_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='id_cliente',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='id_nutricionista',
        ),
        migrations.AddField(
            model_name='agendamento',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='agendamento', to='login.cliente'),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='nutricionista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='agendamento', to='login.nutricionista'),
        ),
    ]
