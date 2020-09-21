from django.db import models
from despesas.models import Despesa


class Instituicao(models.Model):
    instituicao = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)
    despesas = models.ManyToManyField(Despesa)

    def __str__(self):
        return self.instituicao
    
    