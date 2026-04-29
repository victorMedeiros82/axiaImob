from django.shortcuts import render
from imoveis.models import Imovel


def home(request):
    imoveis = Imovel.objects.all()[:6]  # Limita a 6 imóveis para o destaque
    return render(request, "core/home.html", {"imoveis": imoveis})


# Create your views here.
