from django.db import models
from imoveis.models import Imovel


class Documento(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    data_recebimento = models.DateField(null=True, blank=True)
    data_vencimento = models.DateField(null=True, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.imovel.matricula}"
