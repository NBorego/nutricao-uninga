# Generated by Django 5.1 on 2024-09-03 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_alter_cliente_options_alter_nutricionista_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('cliente', 'Pode visitar sua pagina de cliente'), ('nutricionista', 'Pode visitar sua pagina de nutricionista')]},
        ),
    ]
