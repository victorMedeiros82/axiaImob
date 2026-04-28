from django.shortcuts import render

def leilao_list(request):
    # Lógica para listar os leilões
    return render(request, "leiloes/leilao_list.html")


# Create your views here.
