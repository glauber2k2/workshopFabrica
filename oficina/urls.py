from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from carros.api import viewsets as carrosviewsets
from carros.api import viewsets as pessoaviewsets

route = routers.DefaultRouter()

route.register(r'carros', carrosviewsets.CarrosViewSet, basename="carros")
route.register(r'pessoa', pessoaviewsets.PessoaViewSet, basename="pessoa")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))

]
