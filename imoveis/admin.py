# admin.py
from django.contrib import admin
from .models import Imovel
from custos.models import CustoAquisicao, CustoReforma
from django.utils.html import format_html


class CustoAquisicaoAdmin(admin.TabularInline):
    model = CustoAquisicao
    extra = 1


class CustoReformaAdmin(admin.TabularInline):
    model = CustoReforma
    extra = 1


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = (
        "leilao",
        "matricula",
        "tipo",
        "cidade",
        "estado",
        "image_imovel",
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

    # Organiza os campos no formulário para ficar bonitão
    inlines = [CustoAquisicaoAdmin, CustoReformaAdmin]
    fieldsets = (
        (
            "Detalhes do Imóvel",
            {
                "fields": (
                    "leilao",
                    "matricula",
                    "tipo",
                    "area",
                    "estado_conservacao",
                    "situacao_juridica",
                    "image_imovel",
                )
            },
        ),
        (
            "Endereço",
            {
                "fields": (
                    "cep",
                    "logradouro",
                    "numero",
                    "complemento",
                    "bairro",
                    "cidade",
                    "estado",
                )
            },
        ),
        (
            "Geolocalização",
            {"fields": ("latitude", "longitude")},
        ),
    )

    # Aqui é o segredo: injeta o JS no Admin
    def holding_display(self, obj):
        custo = obj.custo_holding_total()

        if custo > 10000:
            cor = "red"
        elif custo > 5000:
            cor = "orange"
        else:
            cor = "green"

        return format_html(f'<strong style="color:{cor}">R$ {custo:,.2f}</strong>')

    holding_display.short_description = "Holding"

    def alerta_display(self, obj):
        status = obj.alerta_holding()

        cores = {"CRÍTICO": "red", "ALTO": "orange", "MODERADO": "gold", "OK": "green"}

        return format_html(f'<strong style="color:{cores[status]}">{status}</strong>')

    alerta_display.short_description = "Alerta"

    class Media:
        js = (
            "admin/js/buscar_cep.js",
        )  # O caminho para o seu JS, coloque na pasta static/js/
