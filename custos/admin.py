from django.contrib import admin
from .models import CustoAquisicao, CustoReforma, CustoHolding


@admin.register(CustoAquisicao)
class CustoAquisicaoAdmin(admin.ModelAdmin):
    list_display = ("imovel", "tipo", "valor", "data")
    list_filter = ("tipo", "data")
    search_fields = ("imovel__matricula",)


@admin.register(CustoReforma)
class CustoReformaAdmin(admin.ModelAdmin):
    list_display = (
        "imovel",
        "descricao",
        "valor_previsto",
        "valor_real",
        "data_inicio",
    )
    list_filter = ("data_inicio", "data_fim")
    search_fields = ("imovel__matricula", "descricao")


@admin.register(CustoHolding)
class CustoHoldingAdmin(admin.ModelAdmin):
    list_display = ("imovel", "tipo", "valor_mensal", "data_inicio", "data_fim")
    list_filter = ("tipo", "data_inicio")
    search_fields = ("imovel__matricula",)
