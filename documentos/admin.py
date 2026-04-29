from django.contrib import admin
from .models import Documento
from axia.admin_base import BaseAdmin
from django.utils.html import format_html


@admin.register(Documento)
class DocumentoAdmin(BaseAdmin):
    list_display = (
        "tipo",
        "imovel",
        "status_badge",
        "data_recebimento",
        "data_vencimento",
    )

    list_filter = ("status", "tipo")
    search_fields = ("tipo", "imovel__matricula")

    ordering = ("-data_recebimento",)
    list_per_page = 20

    autocomplete_fields = ["imovel"]

    # 🔥 PERFORMANCE
    list_select_related = ("imovel",)

    # 🔥 ORGANIZAÇÃO DO FORM
    fieldsets = (
        (
            "📄 Informações do Documento",
            {
                "fields": (
                    ("tipo", "status"),
                    ("imovel",),
                )
            },
        ),
        (
            "📅 Datas",
            {"fields": (("data_recebimento", "data_vencimento"),)},
        ),
        (
            "📎 Arquivo",
            {
                "fields": ("arquivo",),
            },
        ),
    )

    # 🔥 STATUS COM COR (visual profissional)
    def status_badge(self, obj):
        cores = {
            "PENDENTE": "#f39c12",
            "RECEBIDO": "#27ae60",
            "ATRASADO": "#e74c3c",
        }

        cor = cores.get(obj.status, "#555")

        return format_html(
            '<strong style="color:{}">{}</strong>',
            cor,
            obj.status,
        )

    status_badge.short_description = "Status"

    # 🔥 ALERTA AUTOMÁTICO (opcional)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs
