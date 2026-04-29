from django.contrib import admin
from .models import Leilao
from axia.admin_base import BaseAdmin
from django.utils.html import format_html


@admin.register(Leilao)
class LeilaoAdmin(BaseAdmin):
    list_display = (
        "processo",
        "tipo",
        "forma",
        "valor_formatado",
        "data_leilao",
        "status_leilao",
    )

    list_filter = ("tipo", "forma", "data_leilao")
    search_fields = ("processo", "comarca")

    ordering = ("-data_leilao",)
    list_per_page = 20

    autocomplete_fields = ["comarca"]

    # 🔥 ORGANIZAÇÃO DO FORM
    fieldsets = (
        (
            "📄 Dados principais",
            {
                "fields": (
                    ("processo", "tipo"),
                    ("forma", "comarca"),
                )
            },
        ),
        (
            "💰 Valores",
            {
                "fields": ("valor_minimo",),
            },
        ),
        (
            "📅 Datas",
            {
                "fields": ("data_leilao",),
            },
        ),
    )

    # ------------------------------
    # 🎯 VISUAIS
    # ------------------------------

    def valor_formatado(self, obj):
        return format_html(
            '<strong style="color:#2ecc71">R$ {:,.2f}</strong>',
            obj.valor_minimo,
        )

    valor_formatado.short_description = "Valor mínimo"

    def status_leilao(self, obj):
        from datetime import date

        if obj.data_leilao < date.today():
            return format_html('<strong style="color:#7f8c8d">ENCERRADO</strong>')
        elif obj.data_leilao == date.today():
            return format_html('<strong style="color:#e74c3c">HOJE</strong>')
        else:
            return format_html('<strong style="color:#27ae60">ABERTO</strong>')

    status_leilao.short_description = "Status"
