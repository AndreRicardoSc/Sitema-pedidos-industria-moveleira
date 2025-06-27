from django.db import models

from .cliente import Cliente

class Pedido(models.Model):
    quantidade = models.IntegerField(null=False)
    data = models.DateField(null=False)
    cliente = models.ForeignKey(Cliente, null=False, on_delete=models.PROTECT, related_name="pedidos")

    def __str__(self):
        return f"{self.cliente} ({self.data})"