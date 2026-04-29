from django.urls import path
from . import views

urlpatterns = [
    path("", views.custos_list, name="custos_list"),
    path("novo/", views.custo_create, name="custo_create"),
]
