from django.db import models

class MateriaPrima(models.Model):
    descricao = models.CharField(max_length=45, null=False)
    quantidade = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.descricao} ({self.quantidade})"