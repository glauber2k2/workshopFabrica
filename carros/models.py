from django.db import models
from uuid import uuid4
from django.core.validators import RegexValidator

class Pessoa(models.Model):
    cpf = models.CharField(primary_key=True, max_length=255, validators=[RegexValidator(r'^\d{3}\-\d{3}\-\d{3}\-\d{2}$', 'Apenas nesse formato: xxx-xxx-xxx-xx')])
    nome = models.CharField(max_length=255)

class Carros(models.Model):
    id_carro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    modelo = models.CharField(max_length=255)
    problema = models.CharField(max_length=255)
    placa = models.CharField(max_length=7)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)