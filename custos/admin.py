from django.contrib import admin
from .models import CustoAquisicao


@admin.register(CustoAquisicao)
class CustoAquisicaoAdmin(admin.ModelAdmin):
    list_display = ("imovel", "tipo", "valor", "data")
    list_filter = ("tipo", "data")
    search_fields = ("imovel__matricula",)


# admin.site.register(CustoAquisicao, CustoAquisicaoAdmin)
