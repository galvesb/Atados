"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from despesas.api.viewsets import DespesaViewSet, SomaDespesaViewSet, SobraDinheiroViewSet
from instituicoes.api.viewsets import InstituicaoViewSet
from voluntarios.api.viewsets import VoluntarioViewSet, SomaVoluntarioViewSet

router = routers.DefaultRouter()

router.register(r'despesas', DespesaViewSet, basename="despesa")
router.register(r'instituicoes', InstituicaoViewSet, basename="instituicao")
router.register(r'voluntarios', VoluntarioViewSet, basename="voluntarios")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('somaDespesas/', SomaDespesaViewSet.as_view(), name="somadespesas"),
    path('somaVoluntarios/', SomaVoluntarioViewSet.as_view(), name="somavoluntarios"),
    path('sobra/', SobraDinheiroViewSet.as_view(), name="sobra"),
]
