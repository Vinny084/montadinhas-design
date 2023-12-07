from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Moto, RODAS_D
from django.contrib.auth.decorators import login_required
def escolherMoto (request):
    return render(request, 'escolherMoto.html')

def start (request,id):
    moto = Moto.objects.get(id = id)
    print(moto)
    return render (request, 'start.html', {"moto": moto})

def sobre (request):
    return render (request, 'sobre.html')

def mudar_roda_d (request, id, valor):
    moto = Moto.objects.get(pk = id)
    print("editar moto", id, valor)
    if valor == 0:
        moto.roda_d = "static/img/roda/pe/dianteira/preto/preto.png"
    elif valor == 1:
        moto.roda_d = "static/img/roda/pe/dianteira/preto/vermelho.png"
    elif valor ==2 :
        moto.roda_d = "static/img/roda/raiada/dianteira.png"
    else:
        moto.roda_d = "static/img/roda/raiada/paralama/vermelha.png"
    
    moto.save()
    return redirect (f"/app/start/{id}")

@login_required(login_url="/usuarios/login")
def garagem (request):
    if not request.user.is_superuser:
        motos = Moto.objects.filter(usu=request.user)
    else:
         motos = Moto.objects.all()
    
    return render (request, 'garagem.html',{"motos": motos})    