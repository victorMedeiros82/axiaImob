from django.urls import path
from . import views

app_name = "imoveis" # Namespace para evitar conflitos de nomes em URLs

urlpatterns = [
    path("", views.imovel_list, name="imovel_list"),  # Rota para a lista de imóveis
    path(
        "imovel/<int:pk>/", views.imovel_detail, name="imovel_detail"
    ),  # Rota para detalhes do imóvel
]
