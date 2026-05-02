from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required
def redirecionar_apos_login(request):
    """
    Esta view funciona como um 'guarda de trânsito'. 
    Todo mundo cai aqui após o login, e ela manda para o lugar certo.
    """
    if request.user.tipo == 'PROPRIETARIO':
        return redirect('usuarios:painel_proprietario')
    else:
        return redirect('usuarios:painel_inquilino')

def painel_proprietario(request):
    # Aqui você renderiza o HTML que só o dono vê
    return render(request, 'usuarios/painel_proprietario.html')

def painel_inquilino(request):
    # Aqui você renderiza o HTML que só o inquilino vê
    return render(request, 'usuarios/painel_inquilino.html')

from django.shortcuts import render, redirect
from .models import Usuario # Supondo que seu modelo customizado está aqui

def cadastro_usuario(request):
    if request.method == "POST":
        # Pegando os dados comuns
        usuario_digitado = request.POST.get('username')
        tipo_escolhido = request.POST.get('tipo')
        
        # Criando o usuário no banco
        # (Aqui simplificamos, na prática você usaria o UserCreationForm do Django)
        novo_usuario = Usuario.objects.create_user(
            username=usuario_digitado,
            tipo=tipo_escolhido
        )
        
        # Salvando os dados extras de acordo com o tipo
        if tipo_escolhido == 'PROPRIETARIO':
            novo_usuario.cpf_cnpj = request.POST.get('documento_dono')
            # ... salva outros campos
        else:
            novo_usuario.cpf_cnpj = request.POST.get('cpf_inquilino')
            # ... salva outros campos
            
        novo_usuario.save()
        return redirect('login') # Manda para o login após cadastrar

    return render(request, 'usuarios/cadastro.html')