from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_cliente = models.BooleanField(default=False)
    is_nutricionista = models.BooleanField(default=False)

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []       

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(null=True, blank=True, upload_to="cliente_foto/")
    data_nascimento = models.DateField(default='2000-01-01')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Nutricionista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(null=True, blank=True, upload_to="nutricionita_foto/")
    data_nascimento = models.DateField(default='2000-01-01')

    class Meta:
        verbose_name = 'Nutricionista'
        verbose_name_plural = 'Nutricionistas'