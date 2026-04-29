from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin/imoveis/", include("imoveis.urls")),
    path("admin/leiloes/", include("leiloes.urls")),
    path("admin/financeiro/", include("financeiro.urls")),
    path("admin/documentos/", include("documentos.urls")),
    path("admin/custos/", include("custos.urls")),
    path("admin/relatorios/", include("relatorios.urls")),
    path("", include("core.urls")),
    # path("admin/usuarios/", include("usuarios.urls")),
    # path("admin/configuracoes/", include("configuracoes.urls")),
    # path("admin/ajuda/", include("ajuda.urls")),
    # path("admin/suporte/", include("suporte.urls")),
    # path("admin/feedback/", include("feedback.urls")),
]

# Servir arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
