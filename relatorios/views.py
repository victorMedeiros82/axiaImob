from django.shortcuts import render


def relatorio_dashboard(request):
    return render(request, "relatorios/dashboard.html")
