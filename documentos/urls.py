from django.urls import path
from . import views

urlpatterns = [
    path("", views.documentos_list, name="documentos_list"),
    path("novo/", views.documento_create, name="documento_create"),
]
