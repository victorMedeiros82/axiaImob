from django.contrib import admin
from .models import Faturamento 

@admin.register(Faturamento)
class FaturamentoAdmin(admin.ModelAdmin):
    list_display = ("imovel", "tipo", "valor", "data")
    list_filter = ("tipo", "data")
    search_fields = ("imovel__matricula",)

# admin.site.register(Faturamento)