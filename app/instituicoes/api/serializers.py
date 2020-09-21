from rest_framework.serializers import ModelSerializer
from instituicoes.models import Instituicao
from despesas.models import Despesa
from rest_framework import serializers

class InstituicaoSerializer(serializers.ModelSerializer):



    class Meta:
        model = Instituicao

        fields = '__all__'