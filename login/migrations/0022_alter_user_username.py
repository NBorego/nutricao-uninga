# Generated by Django 5.1 on 2024-08-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]