from rest_framework import serializers
from pessoa import models

class PessoaSerializers(serializers.ModelSerializer):
    class Meta:
      model = models.Pessoa
      fields = '__all__'