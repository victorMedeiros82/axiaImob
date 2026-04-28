from django.urls import path
from . import views

urlpatterns = [
    "",
    path("", views.leilao_list, name="leilao_list"),
    path("novo/", views.leilao_create, name="leilao_create"),
    path("<int:pk>/editar/", views.leilao_update, name="leilao_update"),
    path("<int:pk>/excluir/", views.leilao_delete, name="leilao_delete"),
]
