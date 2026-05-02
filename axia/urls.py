from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin/imoveis/", include(("imoveis.urls", "imoveis"), namespace="admin_imoveis"),), # Rota para o admin dos imóveis
    path("admin/leiloes/", include("leiloes.urls")),
    path("admin/financeiro/", include("financeiro.urls")),
    path("admin/documentos/", include("documentos.urls")),
    path("admin/custos/", include("custos.urls")),
    path("admin/relatorios/", include("relatorios.urls")),
    path("", include("core.urls")),
    path("imoveis/", include(("imoveis.urls", "imoveis"), namespace="imoveis")),  # Rota para a lista de imóveis
]

# Servir arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
