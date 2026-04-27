from django.db import models
from imoveis.models import Imovel
from datetime import date

class CustoAquisicao(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    TIPO = [
        ("taxas_cartorio", "Taxas de Cartório"),
        ("impostos", "Impostos"),
        ("honorarios_advogado", "Honorários de Advogado"),
        ("despesas_viagem", "Despesas de Viagem"),
        ("outros", "Outros"),
    ]
    tipo = models.CharField(max_length=100, choices=TIPO, verbose_name="Tipo de Custo")
    valor = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    data = models.DateField("Data")

    def __str__(self):
        return self.tipo


class CustoReforma(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    descricao = models.CharField("Descrição", max_length=100)
    valor_previsto = models.DecimalField(
        "Valor Previsto", max_digits=10, decimal_places=2
    )
    valor_real = models.DecimalField(
        "Valor Real", max_digits=10, decimal_places=2, null=True, blank=True
    )
    data_inicio = models.DateField("Data de Início")
    data_fim = models.DateField("Data de Término", null=True, blank=True)

    def __str__(self):
        return self.descricao


class CustoHolding(models.Model):
    imovel = models.ForeignKey("imoveis.Imovel", on_delete=models.CASCADE)

    tipo = models.CharField(
        max_length=100,
        choices=[
            ("Condominio", "Condomínio"),
            ("IPTU", "IPTU"),
            ("Seguro", "Seguro"),
            ("Utilidades", "Água/Luz"),
            ("Outros", "Outros"),
        ],
    )

    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2)

    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def dias_ativos(self):
        fim = self.data_fim or date.today()
        return (fim - self.data_inicio).days

    def custo_total(self):
        dias = self.dias_ativos()
        custo_dia = self.valor_mensal / 30
        return custo_dia * dias