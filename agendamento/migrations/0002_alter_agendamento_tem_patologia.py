# Generated by Django 5.1 on 2024-09-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='tem_patologia',
            field=models.BooleanField(default=False),
        ),
    ]
