from django.shortcuts import render


def documentos_list(request):
    return render(request, "documentos/documentos_list.html")


def documento_create(request):
    return render(request, "documentos/documento_create.html")


def documento_detail(request, id):
    return render(request, "documentos/documento_detail.html", {"id": id})
