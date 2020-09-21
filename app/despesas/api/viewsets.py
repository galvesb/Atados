from rest_framework.viewsets import ModelViewSet
from despesas.models import Despesa
from voluntarios.models import Voluntario
from django.views.generic import View
from .serializers import DespesaSerializer
from django.db.models import Sum
from django.http import JsonResponse


class DespesaViewSet(ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer


class SomaDespesaViewSet(View):

    def get(self, request):
        total = Despesa.objects.aggregate(Sum('valor'))
        total_decimal = float(total['valor__sum'])
    
        return JsonResponse({'soma': total_decimal})

class SobraDinheiroViewSet(View):

    def get(self, request):
        totalV = Voluntario.objects.aggregate(Sum('dinheiro_doado'))
        total_decimalV = float(totalV['dinheiro_doado__sum'])

        totalD = Despesa.objects.aggregate(Sum('valor'))
        total_decimalD = float(totalD['valor__sum'])

        sobra = float(total_decimalV - total_decimalD)
    
        return JsonResponse({'sobra': round(sobra, 2)})