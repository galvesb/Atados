from rest_framework.serializers import ModelSerializer, ReadOnlyField, SlugRelatedField
from voluntarios.models import Voluntario
from instituicoes.models import Instituicao
from rest_framework import serializers

class VoluntarioSerializer(serializers.ModelSerializer):
    instituicao = serializers.ReadOnlyField(source='instituicao.instituicao')
    
    class Meta:
        
        model = Voluntario
        read_only_fields = ('id', 'instituicao')
        fields = ('id', 'nome', 'sobrenome', 'bairro', 'cidade', 'dinheiro_doado', 'instituicao')