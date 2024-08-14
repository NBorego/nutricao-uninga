from django.db import models
from django.core.validators import MinValueValidator

class Alimento(models.Model):
    nome = models.CharField(max_length=150, null=False, unique=True)
    imagem = models.ImageField(null=True, blank=True, upload_to="imagem__alimento/")
    descricao = models.TextField(null=True)
    calorias = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        validators=[MinValueValidator(0)]
    )
    proteinas = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        validators=[MinValueValidator(0)]
    )
    sodio = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = "Alimento"
        verbose_name_plural = "Alimentos"

    def __str__(self):
        return self.nome
