from rest_framework import serializers
from carros import models

class CarrosSerializers(serializers.ModelSerializer):
    class Meta:
      model = models.Carros
      fields = '__all__'

class PessoaSerializers(serializers.ModelSerializer):
   class Meta:
      model = models.Pessoa
      fields = '__all__'