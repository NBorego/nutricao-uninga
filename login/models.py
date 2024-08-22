from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_cliente = models.BooleanField(default=False)
    is_nutricionista = models.BooleanField(default=False)

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(null=True, blank=True, upload_to="nutricionita_foto/")
    data_nascimento = models.DateField(default='2000-01-01')

class Nutricionista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(null=True, blank=True, upload_to="nutricionita_foto/")
    data_nascimento = models.DateField(default='2000-01-01')
