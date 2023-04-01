from django.db import models
from uuid import uuid4

class Pessoa(models.Model):
    id_pessoa = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    
