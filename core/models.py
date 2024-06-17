from django.db import models
from django.utils import timezone

class ArquivoHash(models.Model):
    hash = models.CharField(max_length=256, unique=True)
    dados = models.JSONField()
    data_carregamento = models.DateTimeField(default=timezone.now)
    usuario = models.CharField(max_length=20,null=True, blank=True)
   