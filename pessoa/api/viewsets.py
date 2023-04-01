from rest_framework import viewsets
from pessoa.api import serializers
from pessoa import models

class PessoaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PessoaSerializers
    queryset = models.Pessoa.objects.all()