# Generated by Django 5.1 on 2024-09-03 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0023_alter_cliente_options_alter_nutricionista_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='nutricionista',
            options={'verbose_name': 'Nutricionista', 'verbose_name_plural': 'Nutricionistas'},
        ),
    ]
