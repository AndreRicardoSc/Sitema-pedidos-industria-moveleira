from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=45, null=False)
    cpf = models.CharField(max_length=11, null=False)
    telefone = models.CharField(max_length=11, null=False)
    email = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"
