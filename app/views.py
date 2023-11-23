from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Moto
def escolherMoto (request):
    return render(request, 'escolherMoto.html')

def start (request,id):
    moto = Moto.objects.get(id = id)
    print(moto)
    return render (request, 'start.html', {"moto": moto})

def sobre (request):
    return render (request, 'sobre.html')

def garagem (request):
    return render (request, 'garagem.html')    