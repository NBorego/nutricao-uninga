from django.db import models
from django.core.validators import MinLengthValidator

class Nutricionista(models.Model):
    usuario = models.CharField(max_length=30, null=False, blank=False)
    foto = models.ImageField(null=True, blank=True, upload_to="nutricionita_foto/")
    email = models.EmailField(max_length=100, null=False, blank=False)
    ra = models.CharField(max_length=15, null=False, blank=False)
    senha = models.CharField(max_length=50, null=False, blank=False, validators=[MinLengthValidator(8)])

    class Meta:
        verbose_name = "Nutricionista"
        verbose_name_plural = "Nutricionistas"

    def __str__(self):
        return self.usuario

class Cliente(models.Model):
    usuario = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    senha = models.CharField(max_length=50, null=False, blank=False, validators=[MinLengthValidator(8)])

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.usuario