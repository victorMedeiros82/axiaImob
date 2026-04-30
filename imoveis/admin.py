from django.contrib import admin
from .models import Imovel
from custos.models import CustoAquisicao, CustoReforma
from django.utils.html import format_html
from axia.admin_base import BaseAdmin


# 🔹 INLINES MAIS ORGANIZADOS
class CustoAquisicaoAdmin(admin.TabularInline):
    model = CustoAquisicao
    extra = 0
    classes = ["collapse"]  # deixa recolhido (UX melhor)


class CustoReformaAdmin(admin.TabularInline):
    model = CustoReforma
    extra = 0
    classes = ["collapse"]


@admin.register(Imovel)
class ImovelAdmin(BaseAdmin):
    list_display = (
        "leilao",
        "matricula",
        "tipo",
        "cidade",
        "estado",
        "image_thumbnail",
        "holding_display",
        "alerta_display",
    )

    list_filter = (
        "tipo",
        "estado_conservacao",
        "situacao_juridica",
        "cidade",
        "estado",
    )

    search_fields = ("leilao__processo", "matricula", "cidade", "estado")

    ordering = ("-id",)
    list_per_page = 20

    # 🔥 MELHORIA IMPORTANTE (evita select gigante)
    autocomplete_fields = ["leilao"]

    # 🔹 INLINES
    inlines = [CustoAquisicaoAdmin, CustoReformaAdmin]

    # 🔥 ORGANIZAÇÃO PROFISSIONAL DOS CAMPOS
    fieldsets = (
        (
            "📄 Dados principais",
            {
                "fields": (
                    ("leilao", "tipo"),
                    ("matricula", "area"),
                    ("estado_conservacao", "situacao_juridica"),
                    ("image_imovel",),
                )
            },
        ),
        (
            "📍 Endereço",
            {
                "fields": (
                    ("cep", "logradouro"),
                    ("numero", "complemento"),
                    ("bairro",),
                    ("cidade", "estado"),
                )
            },
        ),
        (
            "🗺️ Geolocalização",
            {
                "classes": ("collapse",),  # deixa opcional
                "fields": ("latitude", "longitude"),
            },
        ),
    )

    # 🔥 CAMPOS SOMENTE LEITURA (evita bugs)
    readonly_fields = ("image_thumbnail",)

    # 🔥 PERFORMANCE (importante quando crescer)
    list_select_related = ("leilao",)

    # ------------------------------
    # 🎯 VISUAIS
    # ------------------------------

    def holding_display(self, obj):
        custo = obj.custo_holding_total()

        if custo > 10000:
            cor = "#e74c3c"  # vermelho mais bonito
        elif custo > 5000:
            cor = "#f39c12"  # laranja
        else:
            cor = "#27ae60"  # verde

        custo_formatado = f"{custo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return format_html('<strong style="color:{}">R$ {}</strong>', cor, custo_formatado)

    holding_display.short_description = "Holding"

    def alerta_display(self, obj):
        status = obj.alerta_holding()

        cores = {
            "CRÍTICO": "#e74c3c",
            "ALTO": "#f39c12",
            "MODERADO": "#f1c40f",
            "OK": "#27ae60",
        }

        return format_html(
            '<strong style="color:{}">{}</strong>',
            cores.get(status, "#333"),
            status,
        )

    alerta_display.short_description = "Alerta"

    def image_thumbnail(self, obj):
        if obj.image_imovel:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:6px; object-fit:cover;" />',
                obj.image_imovel.url,
            )
        return "-"

    image_thumbnail.short_description = "Imagem"

    # ------------------------------
    # ⚙️ MEDIA (mantém seu JS + BaseAdmin)
    # ------------------------------
    class Media:
        js = ("admin/js/buscar_cep.js",)
