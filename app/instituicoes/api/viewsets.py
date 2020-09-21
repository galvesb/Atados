from rest_framework.viewsets import ModelViewSet
from instituicoes.models import Instituicao
from .serializers import InstituicaoSerializer
from django.db.models import Sum
from django.http import JsonResponse


class InstituicaoViewSet(ModelViewSet):
    queryset = Instituicao.objects.all()
    serializer_class = InstituicaoSerializer