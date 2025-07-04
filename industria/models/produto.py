from django.db import models

from .pedido import Pedido
from .funcionario import Funcionario
from.materia import MateriaPrima

class Produto(models.Model):
    descricao = models.CharField(max_length=45, null=False)
    pedido = models.ForeignKey(Pedido, on_delete= models.PROTECT, related_name="produtos")
    funcionarios = models.ManyToManyField(Funcionario, related_name="produtos")
    materia_prima = models.ManyToManyField(MateriaPrima, related_name="produtos")
    
    def __str__(self):
        return f"{self.descricao} - pedido: {self.pedido}"