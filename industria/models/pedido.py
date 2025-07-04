from django.db import models

from .cliente import Cliente

class Pedido(models.Model):
    descricao = models.CharField(max_length=100, null=False, default="descrição do produto")
    quantidade = models.IntegerField(null=False)
    data = models.DateField(null=False)
    cliente = models.ForeignKey(Cliente, null=False, on_delete=models.PROTECT, related_name="pedidos")

    def __str__(self):
        return f"{self.descricao} ({self.cliente}, {self.data})"