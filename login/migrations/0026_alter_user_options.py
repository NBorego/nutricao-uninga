# Generated by Django 5.1 on 2024-09-03 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0025_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('cliente', 'Pode visitar sua pagina de cliente'), ('nutricionista', 'Pode visitar sua pagina de nutricionista')], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]