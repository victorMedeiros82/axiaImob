from django.contrib import (
    admin,
)  # Importa o módulo admin do Django para registrar modelos no painel de administração
from .models import (
    Faturamento,
)  # Importa o modelo Faturamento para registrá-lo no painel de administração


@admin.register(
    Faturamento
)  # Registra o modelo Faturamento no painel de administração usando o decorador @admin.register
class FaturamentoAdmin(
    admin.ModelAdmin
):  # Define a classe FaturamentoAdmin para personalizar a exibição do modelo Faturamento no painel de administração
    list_display = (
        "imovel",
        "tipo",
        "valor",
        "data",
    )  # Define os campos a serem exibidos na lista de registros de faturamento no painel de administração
    list_filter = (
        "tipo",
        "data",
    )  # Adiciona filtros para os campos "tipo" e "data" no painel de administração, permitindo filtrar os registros de faturamento por tipo e data
    search_fields = (
        "imovel__matricula",
    )  # Adiciona um campo de pesquisa para o campo "matricula" do modelo Imovel, permitindo pesquisar registros de faturamento com base na matrícula do imóvel relacionado


# admin.site.register(Faturamento)
