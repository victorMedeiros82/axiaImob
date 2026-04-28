from django.db import models


class Leilao(models.Model):
    processo = models.CharField(max_length=100)
    comarca = models.CharField(max_length=100)

    TIPO = [
        ("judicial", "Judicial"),
        ("extrajudicial", "Extrajudicial"),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO, default="judicial")

    FORMA = [
        ("presencial", "Presencial"),
        ("online", "Online"),
        ("hibrido", "Híbrido"),
    ]
    forma = models.CharField(max_length=20, choices=FORMA, default="online")

    data_leilao = models.DateTimeField(null=True, blank=True)

    valor_avaliacao = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True
    )
    valor_minimo = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True
    )

    condicoes_pagamento = models.TextField(blank=True)

    link_edital = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.processo or "Sem processo"

    class Meta:
        verbose_name = "Leilão"
        verbose_name_plural = "Leilões"
