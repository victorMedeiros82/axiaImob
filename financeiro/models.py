from django.db import (
    models,
)  # Importa o módulo models do Django para criar modelos de banco de dados
from imoveis.models import (
    Imovel,
)  # Importa o modelo Imovel para criar relacionamentos com o modelo Faturamento


class Faturamento(models.Model): # Define o modelo Faturamento, que representa os registros de faturamento relacionados a imóveis
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    TIPO = [
        ("venda", "Venda"),
        ("locação", "Locação"),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.tipo