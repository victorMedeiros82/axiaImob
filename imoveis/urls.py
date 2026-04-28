from django.urls import path
from . import views

urlpatterns = [
    path("", views.imovel_list, name="imovel_list"),
]
