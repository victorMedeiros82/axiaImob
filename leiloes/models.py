from django.db import models


class Leilao(models.Model):
    processo = models.CharField(
        "Processo",
        max_length=100,
        help_text="Número do processo judicial ou extrajudicial",
    )
    comarca = models.CharField(
        "Comarca",
        max_length=100,
        help_text="Nome da comarca onde o leilão será realizado",
    )
    TIPO = [
        ("judicial", "Judicial"),
        ("extrajudicial", "Extrajudicial"),
    ]
    tipo = models.CharField(
        "Tipo",
        max_length=20,
        choices=TIPO,
        default="judicial",
        help_text="Indica se o leilão é judicial ou extrajudicial",
    )
    FORMA = [
        ("presencial", "Presencial"),
        ("online", "Online"),
        ("hibrido", "Híbrido"),
    ]
    forma = models.CharField(
        "Forma de Realização",
        max_length=20,
        choices=FORMA,
        default="online",
        help_text="Indica se o leilão é presencial, online ou híbrido",
    )
    data_leilao = models.DateTimeField()
    valor_avaliacao = models.DecimalField(
        max_digits=12, decimal_places=2, help_text="Valor de avaliação do imóvel"
    )
    valor_minimo = models.DecimalField(
        max_digits=12, decimal_places=2, help_text="Valor mínimo do leilão"
    )
    condicoes_pagamento = models.TextField(
        "Condições de pagamento",
        max_length=255,
        help_text="Condições de pagamento do leilão",
    )
    link_edital = models.URLField()

    def __str__(self):
        return self.processo


    class Meta:
        verbose_name = "Leilão"
        verbose_name_plural = "Leilões"
