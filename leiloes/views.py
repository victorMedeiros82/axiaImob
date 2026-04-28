from django.shortcuts import render
from django.http import HttpResponse

def leilao_list(request):
    # Lógica para listar os leilões
    return HttpResponse("Lista de Leilões")


# Create your views here.
