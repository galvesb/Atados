from django.db import models
from instituicoes.models import Instituicao


class Voluntario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    dinheiro_doado = models.DecimalField(max_digits=10, decimal_places=2)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
