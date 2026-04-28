from django.contrib import admin
from .models import Leilao


@admin.register(Leilao)
class LeilaoAdmin(admin.ModelAdmin):
    list_display = ("processo", "data_leilao", "valor_minimo", "tipo")
    list_filter = ("tipo", "forma")
    search_fields = ("processo", "comarca")
