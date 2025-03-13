from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def cadastrar(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        email = request.POST["email"]
        senha = request.POST["senha"]

        if User.objects.filter(username=nome).exists():
            return render(request, "cadastro.html", {"error": "Nome já existe"})
        if User.objects.filter(email=email).exists():
            return render(request, "cadastro.html", {"error": "E-mail já cadastrado"})

        User.objects.create_user(username=nome, email=email, password=senha)
        return redirect("home")

    return render(request, "cadastro.html")

def logar(request):
    if request.method == "POST":
        email = request.POST["email"]
        senha = request.POST["senha"]

        user = authenticate(request, username=email, password=senha)  # Correção do uso da variável 'User'
        if user is not None:
            login(request, user)
            return redirect("sessao")
        else:
            return render(request, "login.html", {"erro": "Email ou senha inválidos"})
    
    return render(request, "login.html")

@login_required
def sessao(request):
    return render(request, "sessao.html")

def sair(request):
    logout(request)
    return redirect("logar")


