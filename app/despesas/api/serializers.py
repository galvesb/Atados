from rest_framework.serializers import ModelSerializer
from despesas.models import Despesa
from rest_framework import serializers

class DespesaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Despesa
        fields = ('id', 'nome_conta', 'valor')