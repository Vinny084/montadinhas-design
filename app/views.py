from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Moto, RODAS_D
from .models import Moto, RODAS_T
from .models import Moto, TANQUES
from .models import Moto, CARENAGENS_TRASEIRA
from .models import Moto, FRENTES
from .models import Moto, ESCAPAMENTOS
from .models import Moto, RABETAS
from .models import Moto, ALÇAS
from .models import Moto, TAMPAS_MOTOR
from django.contrib.auth.decorators import login_required
def escolherMoto (request):
    return render(request, 'escolherMoto.html')

def start (request,id):
    moto = Moto.objects.get(id = id)
    print(moto)
    return render (request, 'start.html', {"moto": moto})

def sobre (request):
    return render (request, 'sobre.html')

# roda dianteira
def mudar_roda_d (request, id, valor):
    moto = Moto.objects.get(pk = id)
    print("editar moto", id, valor)
    if valor == 0:
        moto.roda_d = "static/img/roda/pe/dianteira/preto/preto.png"
    elif valor == 1:
        moto.roda_d = "static/img/roda/pe/dianteira/preto/vermelho.png"
    elif valor == 2 :
        moto.roda_d = "static/img/roda/raiada/dianteira.png"
    else:
        moto.roda_d = "static/img/roda/raiada/paralama/vermelha.png"
    
    moto.save()
    return redirect (f"/app/start/{id}")

# roda traseira
def mudar_roda_t (request, id, valor):
    moto = Moto.objects.get(pk = id)
    print("editar moto", id, valor)
    if valor == 0:
        moto.roda_t = "static/img/roda/pe/traseira/preto.png"
    else:
        moto.roda_t = "static/img/roda/raiada/traseira.png"
    
    moto.save()
    return redirect (f"/app/start/{id}")

# tanque
def mudar_tanque (request, id, valor):
    moto = Moto.objects.get(pk = id)
    print("editar moto", id, valor)
    if valor == 0:
        moto.tanque = "static/img/tanque/tanqueStartPreto.png"
    else:
        moto.tanque = "static/img/tanque/tanqueStartVerm.png"
    
    moto.save()
    return redirect (f"/app/start/{id}")

# carenagem traseira
def mudar_carenagemTraseira (request, id, valor):
    moto = Moto.objects.get(pk = id)
    print("editar moto", id, valor)
    if valor == 0:
        moto.carenagemTraseira = "static/img/carenagem/traseira/carenagemTrasPreta.png"
    else:
        moto.carenagemTraseira = "static/img/carenagem/traseira/carenagemTrasVerm.png"
    
    moto.save()
    return redirect (f"/app/start/{id}")

# frente
def mudar_frente (request, id, valor):
    moto = Moto.objects.get(pk = id)
    print("editar moto", id, valor)
    if valor == 0:
        moto.frente = "static/img/frente/frente fan 22/frente fan 22 preta.png"
    elif valor == 1:
        moto.frente = "static/img/frente/frente fan 22/frente fan 22 verm.png"
    elif valor == 2:
        moto.frente = "static/img/frente/frente titan 22/frente titan 22 preta.png"
    elif valor == 3:
        moto.frente = "static/img/frente/frente titan 22/frente titan 22 verm.png"
    elif valor == 4:
        moto.frente = "static/img/frente/frente tw/frente tw preta.png"
    else:
        moto.frente = "static/img/frente/frente tw/frente tw verm.png"
    
    moto.save()
    return redirect (f"/app/start/{id}")

# escapamentos
def mudar_escapamento (request, id, valor):
    moto = Moto.objects.get(pk = id)
    print("editar moto", id, valor)
    if valor == 0:
        moto.escapamento = "static/img/escapamento/original/escapOrigPrata.png"
    elif valor == 1:
        moto.escapamento = "static/img/escapamento/delata/escapDeLata.png"
    elif valor == 2:
        moto.escapamento = "static/img/escapamento/delata/escapDeLataProt.png"
    elif valor == 3:
        moto.escapamento = "static/img/escapamento/delata/escapTorbalEstra.png"
    elif valor == 4:
        moto.escapamento = "static/img/escapamento/dore/escapDoreAzulAT.png"
    elif valor == 5:
        moto.escapamento = "static/img/escapamento/dore/escapDoreVermAT.png"
    elif valor == 6:
        moto.escapamento = "static/img/escapamento/dore/escapDorePretoAT.png"
    else:
        moto.escapamento = "static/img/escapamento/dore/escapDorePolidoAT.png"
    
    moto.save()
    return redirect (f"/app/start/{id}")

# rabeta
def mudar_rabeta (request, id, valor):
    moto = Moto.objects.get(pk = id)
    print("editar moto", id, valor)
    if valor == 0:
        moto.rabeta = "static/img/rabeta/rabetaOrig01.png"
    elif valor == 1:
        moto.rabeta = "static/img/rabeta/rabetaOrig02.png"
    elif valor == 2:
        moto.rabeta = "static/img/rabeta/rabetaOrig03.png"
    elif valor == 3:
        moto.rabeta = "static/img/rabeta/rabetaOrig04.png"
    elif valor == 4:
        moto.rabeta = "static/img/rabeta/rabetaOrig05.png"
    elif valor == 5:
        moto.rabeta = "static/img/rabeta/rabetaOrig06.png"
    elif valor == 6:
        moto.rabeta = "static/img/rabeta/rabetaNvI01.png"
    elif valor == 7:
        moto.rabeta = "static/img/rabeta/rabetaNvI02.png"
    elif valor == 8:
        moto.rabeta = "static/img/rabeta/rabetaNvI03.png"
    elif valor == 9:
        moto.rabeta = "static/img/rabeta/rabetaNvII01.png"
    elif valor == 10:
        moto.rabeta = "static/img/rabeta/rabetaNvII02.png"
    elif valor == 11:
        moto.rabeta = "static/img/rabeta/rabetaNvII03.png"
    elif valor == 12:
        moto.rabeta = "static/img/rabeta/rabetaNvII04.png"
    elif valor == 13:
        moto.rabeta = "static/img/rabeta/rabetaNvII05.png"
    elif valor == 14:
        moto.rabeta = "static/img/rabeta/rabetaNvIII01.png"
    elif valor == 15:
        moto.rabeta = "static/img/rabeta/rabetaNvIII02.png"
    else:
        moto.rabeta = "static/img/rabeta/rabetaNvIII03.png"
    
    moto.save()
    return redirect (f"/app/start/{id}")

# rabeta
def mudar_alca (request, id, valor):
    moto = Moto.objects.get(pk = id)
    print("editar moto", id, valor)
    if valor == 0:
        moto.alca = "static/img/alca/alcaOrigPreta.png"
    elif valor == 1:
        moto.alca = "static/img/alca/alcaOrigCromo.png"
    elif valor == 2:
        moto.alca = "static/img/alca/alcaAltaPreta.png"
    elif valor == 3:
        moto.alca = "static/img/alca/alcaAltaCromo.png"
    elif valor == 4:
        moto.alca = "static/img/alca/alcaTitanPreta.png"
    elif valor == 5:
        moto.alca = "static/img/alca/alcaTitanPrata.png"
    elif valor == 6:
        moto.alca = "static/img/alca/churrasqueiraCromo.png"
    elif valor == 7:
        moto.alca = "static/img/alca/churrasqueiraCromoGivi.png"
    elif valor == 8:
        moto.alca = "static/img/alca/churrasqueiraCromoGiviBau.png"
    elif valor == 9:
        moto.alca = "static/img/alca/churrasqueiraCromoSup.png"
    elif valor == 10:
        moto.alca = "static/img/alca/churrasqueiraCromoSupBau.png"
    elif valor == 11:
        moto.alca = "static/img/alca/churrasqueiraPreta.png"
    elif valor == 12:
        moto.alca = "static/img/alca/churrasqueiraPretaGivi.png"
    elif valor == 13:
        moto.alca = "static/img/alca/churrasqueiraPretaGiviBau.png"
    elif valor == 14:
        moto.alca = "static/img/alca/churrasqueiraPretaSup.png"
    else:
        moto.alca = "static/img/alca/churrasqueiraPretaSupBau.png"
    
    moto.save()
    return redirect (f"/app/start/{id}")

# tanque
def mudar_tampaMotor (request, id, valor):
    moto = Moto.objects.get(pk = id)
    print("editar moto", id, valor)
    if valor == 0:
        moto.tampaMotor = "static/img/vazio.png"
    else:
        moto.tampaMotor = "static/img/motor/tampaLateral/tampaPretaMotor.png"
    
    moto.save()
    return redirect (f"/app/start/{id}")

@login_required(login_url="/usuarios/login")
def garagem (request):
    if not request.user.is_superuser:
        motos = Moto.objects.filter(usu=request.user)
    else:
         motos = Moto.objects.all()
    
    return render (request, 'garagem.html',{"motos": motos})    

@login_required(login_url="/usuarios/login")
def novo (request):
    nova = Moto( 
        titulo = "sem nome", 
        roda_t = "static/img/roda/raiada/traseira.png", 
        roda_d = "static/img/roda/raiada/dianteira.png",
        rabeta = "static/img/rabeta/rabetaOrig01.png",
        alca = "static/img/alca/alcaOrigPreta.png",
        carenagemTraseira = "static/img/carenagem/traseira/carenagemTrasPreta.png",
        frente = "static/img/frente/frente fan 22/frente fan 22 preta.png",
        escapamento = "static/img/escapamento/original/escapOrigPrata.png",
        tampaMotor = "static/img/vazio.png",
        tanque = "static/img/tanque/tanqueStartPreto.png",
        usu = request.user)
    nova.save()

    return redirect(f"/app/start/{nova.id}")