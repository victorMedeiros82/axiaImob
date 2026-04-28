from django.shortcuts import render
from .models import Faturamento


def faturamento_list(request):
    faturamentos = Faturamento.objects.all()
    return render(
        request, "financeiro/faturamento_list.html", {"faturamentos": faturamentos}
    )
