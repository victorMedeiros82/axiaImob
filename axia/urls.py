from django.contrib import admin
from django.urls import path, include

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
