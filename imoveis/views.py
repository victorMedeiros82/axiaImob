from django.shortcuts import render
from .models import Imovel


def imovel_list(request):
    imoveis = Imovel.objects.all()
    return render(request, "imoveis/imovel_list.html", {"imoveis": imoveis})
