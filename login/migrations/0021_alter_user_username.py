# Generated by Django 5.1 on 2024-08-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_alter_user_managers_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
