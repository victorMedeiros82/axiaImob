from django.shortcuts import render
from .models import Leilao


def leilao_list(request):
    leiloes = Leilao.objects.all()
    return render(request, "leiloes/leilao_list.html", {"leiloes": leiloes})
