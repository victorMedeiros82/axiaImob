from django.contrib import admin
from axia.admin_base import BaseAdmin
from .models import CustoAquisicao, CustoReforma, CustoHolding
from django.utils.html import format_html


@admin.register(CustoAquisicao)
class CustoAquisicaoAdmin(BaseAdmin):
    list_display = ("imovel", "tipo", "valor_formatado", "data")
    list_filter = ("tipo", "data")
    search_fields = ("imovel__matricula",)

    ordering = ("-data",)
    list_per_page = 20

    autocomplete_fields = ["imovel"]
    list_select_related = ("imovel",)

    fieldsets = (
        (
            "💰 Dados do custo",
            {
                "fields": (
                    ("imovel", "tipo"),
                    ("valor",),
                    ("data",),
                )
            },
        ),
    )

    def valor_formatado(self, obj):
        return format_html(
            '<strong style="color:#e74c3c">R$ {:,.2f}</strong>',
            obj.valor,
        )

    valor_formatado.short_description = "Valor"


@admin.register(CustoReforma)
class CustoReformaAdmin(BaseAdmin):
    list_display = (
        "imovel",
        "descricao",
        "valor_previsto_formatado",
        "valor_real_formatado",
        "status_custo",
        "data_inicio",
    )

    list_filter = ("data_inicio", "data_fim")
    search_fields = ("imovel__matricula", "descricao")

    ordering = ("-data_inicio",)
    list_per_page = 20

    autocomplete_fields = ["imovel"]
    list_select_related = ("imovel",)

    fieldsets = (
        (
            "🏗️ Reforma",
            {
                "fields": (
                    ("imovel",),
                    ("descricao",),
                )
            },
        ),
        ("💰 Valores", {"fields": (("valor_previsto", "valor_real"),)}),
        ("📅 Datas", {"fields": (("data_inicio", "data_fim"),)}),
    )

    def valor_previsto_formatado(self, obj):
        return format_html(
            '<span style="color:#f39c12">R$ {:,.2f}</span>',
            obj.valor_previsto or 0,
        )

    def valor_real_formatado(self, obj):
        return format_html(
            '<strong style="color:#e74c3c">R$ {:,.2f}</strong>',
            obj.valor_real or 0,
        )

    def status_custo(self, obj):
        if obj.valor_real and obj.valor_previsto:
            if obj.valor_real > obj.valor_previsto:
                return format_html('<strong style="color:#e74c3c">ACIMA</strong>')
            elif obj.valor_real < obj.valor_previsto:
                return format_html('<strong style="color:#27ae60">ABAIXO</strong>')
        return format_html('<span style="color:#7f8c8d">OK</span>')

    status_custo.short_description = "Status"


@admin.register(CustoHolding)
class CustoHoldingAdmin(BaseAdmin):
    list_display = (
        "imovel",
        "tipo",
        "valor_mensal_formatado",
        "data_inicio",
        "data_fim",
        "custo_total_estimado",
    )

    list_filter = ("tipo", "data_inicio")
    search_fields = ("imovel__matricula",)

    ordering = ("-data_inicio",)
    list_per_page = 20

    autocomplete_fields = ["imovel"]
    list_select_related = ("imovel",)

    fieldsets = (
        (
            "🏠 Holding",
            {
                "fields": (
                    ("imovel", "tipo"),
                    ("valor_mensal",),
                )
            },
        ),
        ("📅 Período", {"fields": (("data_inicio", "data_fim"),)}),
    )

    def valor_mensal_formatado(self, obj):
        return format_html(
            '<strong style="color:#e67e22">R$ {:,.2f}</strong>',
            obj.valor_mensal,
        )

    def custo_total_estimado(self, obj):
        from datetime import date

        if not obj.data_inicio:
            return "-"

        fim = obj.data_fim or date.today()
        meses = (fim.year - obj.data_inicio.year) * 12 + (
            fim.month - obj.data_inicio.month
        )

        total = meses * obj.valor_mensal

        return format_html(
            '<strong style="color:#c0392b">R$ {:,.2f}</strong>',
            total,
        )

    custo_total_estimado.short_description = "Total"
