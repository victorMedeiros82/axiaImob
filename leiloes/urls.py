from django.urls import path
from . import views

urlpatterns = [
    path("", views.leilao_list, name="leilao_list"),
]
