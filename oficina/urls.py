from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from carros.api import viewsets as carrosviewsets
from pessoa.api import viewsets as pessoaviewsets

route = routers.DefaultRouter()

route.register(r'carros', carrosviewsets.CarrosViewSet, basename="Carros")
route.register(r'pessoa', pessoaviewsets.PessoaViewSet, basename="Pessoa")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))

]
