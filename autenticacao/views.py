from django.shortcuts import render
from django.http import HttpResponse
from .utils import password_is_valid
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.shortcuts import render
from django.contrib import auth
from . import views


def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
		    return redirect('/')
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro')
        try:
            user = User.objects.create_user(username=username,
                                            
                                            password=senha,
                                            is_active=False)
            user.save()
            messages.add(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
            
            return redirect('/auth/logar')
        except:
            messages.add(request, constants.ERROR, 'Erro interno no sistema')
            return redirect('/auth/cadastro')

            
def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
		return redirect('/')
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        usuario = auth.authenticate(username=username, password=senha)

    if not usuario:
        messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
        return redirect('/auth/logar')
    else:
        auth.login(request, usuario)
        return redirect('/')
    
    def sair(request):
        auth.logout(request)
        return redirect('/auth/logar')