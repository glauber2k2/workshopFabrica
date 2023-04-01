from django.db import models
from uuid import uuid4

class Carros(models.Model):
    id_carro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    modelo = models.CharField(max_length=255)
    problema = models.CharField(max_length=255)
    placa = models.CharField(max_length=7)
    
