from django.urls import path
from . import views

urlpatterns = [
    path("", views.documentos_list, name="documentos_list"),
    path("novo/", views.documento_create, name="documento_create"),
    path("<int:id>/", views.documento_detail, name="documento_detail"),
]
