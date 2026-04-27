from django.db import models # Importa o módulo models do Django para criar modelos de banco de dados
from imoveis.models import Imovel # Importa o modelo Imovel para criar relacionamentos com o modelo Faturamento


class Faturamento(models.Model): # Define o modelo Faturamento, que representa os registros de faturamento relacionados a imóveis
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE) # Cria um campo de chave estrangeira para o modelo Imovel, permitindo relacionar cada registro de faturamento a um imóvel específico. O parâmetro on_delete=models.CASCADE garante que, se um imóvel for excluído, os registros de faturamento relacionados também serão excluídos.
    tipo = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateField()

