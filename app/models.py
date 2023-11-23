from django.db import models

RODAS_T=[
    ("static/img/roda/pe/traseira/preto.png", "pe traseira"),
    ("static/img/roda/raiada/traseira.png", "raiada traseira"),
    
]

RODAS_D =[
    ("static/img/roda/pe/dianteira/preto/preto.png", "pe dianteira"),
    ("static/img/roda/raiada/dianteira.png", "raiada diateira"),
]

PARALAMAS =[
    ("static/img/roda/pe/dianteira/preto/preto.png", "pe preto"),
    ("static/img/roda/pe/dianteira/preto/vermelho.png", "pe vermelho"),
    ("static/img/roda/raiada/dianteira.png", "raiada preto"),
    ("static/img/roda/raiada/paralama/vermelha.png", "raiada vermelho"),
]

TANQUES =[
    ("static/img/tanque/tanqueStartPreto.png", "PRETO"),
    ("static/img/tanque/tanqueStartVerm.png", "VERMELHO"),
]

CARENAGENS_TRASEIRA =[
    ("static/img/carenagem/traseira/carenagemTrasPreta.png", "PRETO"),
    ("static/img/carenagem/traseira/carenagemTrasVerm.png", "VERMELHO"),
]

RABETAS =[
    ("static/img/rabeta/rabetaOrig01.png", "Orig01"),
    ("static/img/rabeta/rabetaOrig02.png", "Orig02"),
    ("static/img/rabeta/rabetaOrig03.png", "Orig03"),
    ("static/img/rabeta/rabetaOrig04.png", "Orig04"),
    ("static/img/rabeta/rabetaOrig05.png", "Orig05"),
    ("static/img/rabeta/rabetaOrig06.png", "Orig06"),
    ("static/img/rabeta/rabetaNvI01.png", "NvI01"),
    ("static/img/rabeta/rabetaNvI02.png", "NvI02"),
    ("static/img/rabeta/rabetaNvI03.png", "NvI03"),
    ("static/img/rabeta/rabetaNvII01.png", "NvII01"),
    ("static/img/rabeta/rabetaNvII02.png", "NvII02"),
    ("static/img/rabeta/rabetaNvII03.png", "NvII03"),
    ("static/img/rabeta/rabetaNvII04.png", "NvII04"),
    ("static/img/rabeta/rabetaNvII05.png", "NvII05"),
    ("static/img/rabeta/rabetaNvIII01.png", "NvIII01"),
    ("static/img/rabeta/rabetaNvIII02.png", "NvII02"),
    ("static/img/rabeta/rabetaNvIII03.png", "NvIII03"),
]

ALÇAS =[
    ("static/img/alca/alcaOrigPreta.png", "preto"),
    ("static/img/alca/alcaOrigCromo.png", "cromo"),
    ("static/img/alca/alcaAltaPreta.png", "alta preta"),
    ("static/img/alca/alcaAltaCromo.png", "alta cromo"),
    ("static/img/alca/churrasqueiraCromo.png", "churrasqueira cromo"),
    ("static/img/alca/churrasqueiraCromoGivi.png", "churrasqueira cromo givi"),
    ("static/img/alca/churrasqueiraCromoGiviBau.png", "churrasqueira cromo givi bau"),
    ("static/img/alca/churrasqueiraCromoSup.png", "churrasqueira cromo suporte"),
    ("static/img/alca/churrasqueiraCromoSupBau.png", "churrasqueira cromo suporte bau"),
    ("static/img/alca/churrasqueiraPreta.png", "churrasqueira preta"),
    ("static/img/alca/churrasqueiraPretaGivi.png", "churrasqueira preta givi"),
    ("static/img/alca/churrasqueiraPretaGiviBau.png", "churrasqueira preta givi bau"),
    ("static/img/alca/churrasqueiraPretaSup.png", "churrasqueira preta suporte"),
    ("static/img/alca/churrasqueiraPretaSupBau.png", "churrasqueira preta suporte bau"),
]

FRENTES = [
    ("static/img/frente/frente fan 22/frente fan 22 preta.png", "Fan preta"),
    ("static/img/frente/frente fan 22/frente fan 22 verm.png","Fan vermelha"),
    ("static/img/frente/frente titan 22/frente titan 22 preta.png","Titan preta"), 
    ("static/img/frente/frente titan 22/frente titan 22 verm.png", "Titan vermelha"),
    ("static/img/frente/frente tw/frente tw preta.png", "Twister preta"),
    ("static/img/frente/frente tw/frente tw verm.png", "Twister vermelha"),        
]

ESCAPAMENTOS =[
    ("static/img/escapamento/original/escapOrigPrata.png", "original"),
    ("static/img/escapamento/delata/escapDeLata.png", "delata"),
    ("static/img/escapamento/delata/escapDeLataProt.png", "delata com protecao"),
    ("static/img/escapamento/delata/escapTorbalEstra.png", "torbal"),
    ("static/img/escapamento/dore/escapDoreAzulAT.png", "dore azul"),
    ("static/img/escapamento/dore/escapDoreVermAT.png", "dore vermelho"),
    ("static/img/escapamento/dore/escapDorePretoAT.png", "dore preto"),
    ("static/img/escapamento/dore/escapDorePolidoAT.png", "dore prata"),
]

TAMPAS_MOTOR =[
    ("static/img/vazio.png", "prata"),
    ("static/img/motor/tampaLateral/tampaPretaMotor.png", "preta"),
]


class Moto(models.Model):
    roda_t = models.CharField("Roda Traseira", choices=RODAS_T, max_length=150)
    roda_d = models.CharField("Roda Dianteira", choices=RODAS_D, max_length=150)
    paralama = models.CharField(choices=PARALAMAS, max_length=150)
    carenagemTraseira = models.CharField(choices=CARENAGENS_TRASEIRA, max_length=150)
    frente = models.CharField(choices=FRENTES, max_length=150)
    escapamento = models.CharField(choices=ESCAPAMENTOS, max_length=150)
    tampaMotor = models.CharField(choices=TAMPAS_MOTOR, max_length=150)
    

class Start(Moto):
    tanque = models.CharField(choices=TANQUES, max_length=150)
        

# class Fan(Moto):
#     pass

# class Titan(Moto):
#     pass

class Projeto(models.Model):
    moto = models.ForeignKey(
        "Moto",
        on_delete=models.CASCADE,
    )