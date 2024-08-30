from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_cliente = models.BooleanField(default=False)
    is_nutricionista = models.BooleanField(default=False)

    username = models.CharField(unique=True, max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    foto = models.ImageField(null=True, blank=True, upload_to="foto_usuario/")
    data_nascimento = models.DateField(null=False, blank=False, default='2000-01-01')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

        permissions = [
            ("cliente", "Pode visitar sua pagina de cliente"),
        ]

    def __str__(self):
        return self.user.email

class Nutricionista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Nutricionista'
        verbose_name_plural = 'Nutricionistas'

        permissions = [
            ("nutricionista", "Pode visitar sua pagina de nutricionista"),
        ]

    def __str__(self):
        return self.user.email