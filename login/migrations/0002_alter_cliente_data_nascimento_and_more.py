# Generated by Django 5.1 on 2024-08-22 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_nascimento',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='nutricionista',
            name='data_nascimento',
            field=models.DateField(default='2000-01-01'),
        ),
    ]
