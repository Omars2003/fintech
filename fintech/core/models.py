# core/models.py
from django.db import models
from django.conf import settings

class ProductoFinanciero(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tasa_retorno = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Tasa de retorno anual en porcentaje"
    )
    plazo = models.IntegerField(help_text="Plazo de inversión en meses")
    riesgo = models.CharField(
        max_length=50,
        choices=[('bajo', 'Bajo'), ('medio', 'Medio'), ('alto', 'Alto')],
        default='medio'
    )

    def __str__(self):
        return f"{self.nombre} - Riesgo: {self.riesgo}"


class Inversion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    producto_financiero = models.ForeignKey(ProductoFinanciero, on_delete=models.CASCADE)
    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Monto invertido en moneda local"
    )
    fecha_inversion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Inversión de {self.usuario.username} en {self.producto_financiero.nombre} por ${self.monto}"
