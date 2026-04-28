from django.urls import path
from . import views

urlpatterns = [
    path("", views.faturamento_list, name="faturamento_list"),
]
