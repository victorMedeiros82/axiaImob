from django.contrib import admin
from .models import Faturamento
from axia.admin_base import BaseAdmin
from django.utils.html import format_html


@admin.register(Faturamento)
class FaturamentoAdmin(BaseAdmin):
    list_display = (
        "imovel",
        "tipo",
        "valor_formatado",
        "data",
        "status_financeiro",
    )

    list_filter = (
        "tipo",
        "data",
    )

    search_fields = ("imovel__matricula",)

    ordering = ("-data",)
    list_per_page = 20

    autocomplete_fields = ["imovel"]

    # 🔥 PERFORMANCE
    list_select_related = ("imovel",)

    # 🔥 ORGANIZAÇÃO DO FORM
    fieldsets = (
        (
            "💰 Dados financeiros",
            {
                "fields": (
                    ("imovel", "tipo"),
                    ("valor",),
                    ("data",),
                )
            },
        ),
    )

    # ------------------------------
    # 🎯 VISUAIS
    # ------------------------------

    def valor_formatado(self, obj):
        valor_formatado = f"{obj.valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return format_html(
            '<strong style="color:#2ecc71">R$ {}</strong>',
            valor_formatado,
        )

    valor_formatado.short_description = "Valor"

    def status_financeiro(self, obj):
        # exemplo simples (você pode evoluir isso depois)
        if obj.valor > 10000:
            return format_html('<strong style="color:#27ae60">ALTO</strong>')
        elif obj.valor > 5000:
            return format_html('<strong style="color:#f39c12">MÉDIO</strong>')
        else:
            return format_html('<strong style="color:#e74c3c">BAIXO</strong>')

    status_financeiro.short_description = "Status"
