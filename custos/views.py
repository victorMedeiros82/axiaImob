from django.shortcuts import (
    render,
)  # importando a função render para renderizar os templates


def custos_list(request):
    return render(request, "custos/custos_list.html")


def custo_create(request):
    return render(request, "custos/custo_create.html")
