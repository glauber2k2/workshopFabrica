from rest_framework import viewsets
from carros.api import serializers
from carros import models

class CarrosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CarrosSerializers
    queryset = models.Carros.objects.all()

class PessoaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PessoaSerializers
    queryset = models.Pessoa.objects.all()