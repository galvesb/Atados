from rest_framework.viewsets import ModelViewSet
from voluntarios.models import Voluntario
from django.views.generic import View
from .serializers import VoluntarioSerializer
from django.db.models import Sum
from django.http import JsonResponse


class VoluntarioViewSet(ModelViewSet):
    queryset = Voluntario.objects.all()
    serializer_class = VoluntarioSerializer


class SomaVoluntarioViewSet(View):

    def get(self, request):
        total = Voluntario.objects.aggregate(Sum('dinheiro_doado'))
        total_decimal = float(total['dinheiro_doado__sum'])
    
        return JsonResponse({'soma': total_decimal})