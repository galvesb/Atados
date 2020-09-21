from django.db import models

class Despesa(models.Model):
    nome_conta = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome_conta
