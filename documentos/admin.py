from django.contrib import admin
from .models import Documento


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("tipo", "imovel", "status", "data_recebimento", "data_vencimento")
    list_filter = ("status",)
    search_fields = ("tipo", "imovel__matricula")
