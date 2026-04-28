from django.contrib import admin
from .models import Leilao


@admin.register(Leilao)
class LeilaoAdmin(admin.ModelAdmin):
    list_display = ("imovel", "data_leilao", "valor_inicial", "status")
    list_filter = ("status",)
    search_fields = ("imovel__matricula",)
