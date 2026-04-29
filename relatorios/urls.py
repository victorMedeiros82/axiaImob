from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.relatorio_dashboard, name="relatorio_dashboard"),
]
