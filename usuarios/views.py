import email
from os import name
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
def index (request): 
    if request.method == 'POST':
        nome  = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']

        if not nome.strip():
            print("O campo nome não pode ficar em branco")
            return redirect('index')
        if not email.strip():
            print('O email não pode ficar em branco')
            return redirect('index')
        if not senha.strip():
            print('A senha não pode ficar em branco')
            return redirect('index')


        if User.objects.filter(email=email).exists():
            print('usuario já cadastrado')
            return redirect('index')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        if user is not None:
                auth.login(request, user)
                return redirect ('login')
        return redirect ('index') 
    else:
        return render (request,'index.html')

def login (request):
    if request.method == 'POST':
        email  = request.POST['email']
        senha = request.POST['password']

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()

            user = auth.authenticate(request, username=nome, password=senha)
        
            if user is not None:
                auth.login(request, user)
                return redirect ('garagem') 
        return redirect ('login')
    else:
        return render (request, 'login.html')

@login_required(login_url="/login")
def sair(request):
    logout(request)
    return redirect('login')