from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

def cadastro(request):
    if request.method == 'GET':
        print(request.user)
        return render(request, 'cadastro.html')
    elif request.method == 'POST':

        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senha e Confirmar senha não coincidem')
            return redirect('/usuarios/cadastro')

        user = User.objects.filter(username=nome)
        print(user)
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existente')
            return redirect('/usuarios/cadastro')

        try:
            User.objects.create_user(
                username=nome,
                password=senha
            )
            return redirect('/usuarios/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do Servidor')
            return redirect('/usuarios/cadastro')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=nome, password=senha)

        if user:
            auth.login(request, user)
            # messages.add_message(request, constants.SUCCESS, 'Logado')
            return redirect('/flashcards/novo_flashcard/')
        else:
            messages.add_message(request, constants.ERROR, 'Nome ou Senha inválidos')
            return redirect('/usuarios/login')

def logout(request):
    auth.logout(request)
    return redirect('/usuarios/login')