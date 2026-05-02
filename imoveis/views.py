from django.shortcuts import render
from .models import Imovel


def imovel_list(request):
    imoveis = Imovel.objects.all()
    return render(request, "imoveis/imovel_list.html", {"imoveis": imoveis})


def imovel_detail(request, pk): # Rota para detalhes do imóvel
    imovel = Imovel.objects.get(pk=pk) # Busca o imóvel pelo ID (pk) passado na URL
    return render(request, "imoveis/imovel_detail.html", {"imovel": imovel}) # Renderiza a página de detalhes do imóvel