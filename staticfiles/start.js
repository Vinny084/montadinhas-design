/*-----------------------------------*/
/*Rodas*/

$('#rodas').hide();

$('#btRodas').click(function(){
    $('#rodas').show();
    $('#selecPecas').hide();
});

$('#voltarRodas').click(function(){
    $('#selecPecas').show();
    $('#rodas').hide();
});


// roda dianteira
// const peDianteiraParalamaPreto = document.querySelector("#peDianteiraParalamaPreto");
// const peDianteiraParalamaVermelho = document.querySelector("#peDianteiraParalamaVermelho");
// const raiadaDianteiraParalamaPreto = document.querySelector("#raiadaDianteiraParalamaPreto");
// const RaiadaDianteiraParalamaPreto = document.querySelector("#raiadaDianteiraParalamaPreto");
// const raiadaDianteiraParalamaVermelho = document.querySelector("#raiadaDianteiraParalamaVermelho");

// peDianteiraParalamaPreto.addEventListener("click", function(){
//     RaiadaDianteiraParalamaPreto.setAttribute("src", "../img/roda/pe/dianteira/preto/preto.png");
// });

// peDianteiraParalamaVermelho.addEventListener("click", function(){
//     RaiadaDianteiraParalamaPreto.setAttribute("src", "../img/roda/pe/dianteira/preto/vermelho.png");
// });

// raiadaDianteiraParalamaPreto.addEventListener("click", function(){
//     RaiadaDianteiraParalamaPreto.setAttribute("src", "../img/roda/raiada/dianteira.png");
// });


// raiadaDianteiraParalamaVermelho.addEventListener("click", function(){
//     RaiadaDianteiraParalamaPreto.setAttribute("src", "../img/roda/raiada/paralama/vermelha.png");
// });

// roda dianteira
$('#rodaDianteira').hide();

$('#rodaFrente').click(function(){
    $('#rodaDianteira').show();
    $('#rodas').hide();
});

$('#voltarRodaD').click(function(){
    $('#rodas').show();
    $('#rodaDianteira').hide();
});

/*roda traseira*/
// const raiadaT = document.querySelector("#raiadaT");
// const raiadaTras = document.querySelector("#raiadaTras");
// const peTPreto = document.querySelector("#peTPreto");

// peTPreto.addEventListener("click", function(){
//     raiadaT.setAttribute("src", "../img/roda/pe/traseira/preto.png");
// });

// raiadaTras.addEventListener("click", function(){
//     raiadaT.setAttribute("src", "../img/roda/raiada/traseira.png");
// });

/*roda traseira*/
$('#rodaTraseira').hide();

$('#rodaTras').click(function(){
    $('#rodaTraseira').show();
    $('#rodas').hide();
});

$('#voltarRodaT').click(function(){
    $('#rodas').show();
    $('#rodaTraseira').hide();
});

/*tanque*/
// const tanqueStartPreto = document.querySelector("#tanqueStartPreto");
// const tanqueStartpreto = document.querySelector("#tanqueStartpreto");
// const tanqueStartVerm = document.querySelector("#tanqueStartVerm");

// tanqueStartpreto.addEventListener("click", function(){
//     tanqueStartPreto.setAttribute("src", "../img/tanque/tanqueStartPreto.png");
// });

// tanqueStartVerm.addEventListener("click", function(){
//     tanqueStartPreto.setAttribute("src", "../img/tanque/tanqueStartVerm.png");
// });
// /*-----------------------------------*/
/*Tanque*/

$('#tanque').hide();

$('#btTanque').click(function(){
    $('#tanque').show();
    $('#selecPecas').hide();
});

$('#voltarTanque').click(function(){
    $('#selecPecas').show();
    $('#tanque').hide();
});

/*carenagem traseira*/
// const carenagemTrasVerm = document.querySelector("#carenagemTrasVerm");
// const carenagemTrasPreta = document.querySelector("#carenagemTrasPreta");
// const carenagemTraspreta = document.querySelector("#carenagemTraspreta");

// carenagemTrasVerm.addEventListener("click", function(){
//     carenagemTrasPreta.setAttribute("src", "../img/carenagem/traseira/carenagemTrasVerm.png");
// });

// carenagemTraspreta.addEventListener("click", function(){
//     carenagemTrasPreta.setAttribute("src", "../img/carenagem/traseira/carenagemTrasPreta.png");
// });

/*-----------------------------------*/
/*Carenagem Traseira*/

$('#carenagemTras').hide();

$('#btCarenagemT').click(function(){
    $('#carenagemTras').show();
    $('#selecPecas').hide();
});

$('#voltarCarenagemT').click(function(){
    $('#selecPecas').show();
    $('#carenagemTras').hide();
});

/*-----------------------------------*/
/*Escolher frente*/

$('#frente').hide();

$('#btFrente').click(function(){
    $('#frente').show();
    $('#selecPecas').hide();
});

$('#voltarFrente').click(function(){
    $('#selecPecas').show();
    $('#frente').hide();
});


/*frente fan*/
// const frenteFan22Preta = document.querySelector("#frenteFan22Preta");
// const frenteFan22Verm = document.querySelector("#frenteFan22Verm");
// const frenteFan22preta = document.querySelector("#frenteFan22preta");

// frenteFan22preta.addEventListener("click", function(){
//     frenteFan22Preta.setAttribute("src", "img/frente/frente fan 22/frente fan 22 preta.png");
// });

// frenteFan22Verm.addEventListener("click", function(){
//     frenteFan22Preta.setAttribute("src", "img/frente/frente fan 22/frente fan 22 Verm.png");
// });

/*-----------------------------------*/
/*Frente Fan*/

$('#frenteFan').hide();

$('#frentefan22').click(function(){
    $('#frenteFan').show();
    $('#frente').hide();
});

$('#voltarFrenteFan').click(function(){
    $('#frente').show();
    $('#frenteFan').hide(); 
});


/*frente titan 22*/
// const frenteTitan22Preta = document.querySelector("#frenteTitan22Preta");
// const frenteTitan22preta = document.querySelector("#frenteTitan22preta");
// const frenteTitan22Verm = document.querySelector("#frenteTitan22Verm");


// frenteTitan22preta.addEventListener("click", function(){
//     frenteFan22Preta.setAttribute("src", "../img/frente/frente titan 22/frente titan 22 preta.png");
// });

// frenteTitan22Verm.addEventListener("click", function(){
//     frenteFan22Preta.setAttribute("src", "../img/frente/frente titan 22/frente titan 22 Verm.png");
// });


/*-----------------------------------*/
/*Frente Titan 22*/

$('#frenteTitan').hide();

$('#frentetitan22').click(function(){
    $('#frenteTitan').show();
    $('#frente').hide();
});

$('#voltarFrenteTitan22').click(function(){
    $('#frente').show();
    $('#frenteTitan').hide();
});


/*frente tw*/
// const frenteTwPreta = document.querySelector("#frenteTwPreta");
// const frenteTwpreta = document.querySelector("#frenteTwpreta");
// const frenteTwVerm = document.querySelector("#frenteTwVerm");


// frenteTwpreta.addEventListener("click", function(){
//     frenteFan22Preta.setAttribute("src", "../img/frente/frente tw/frente tw preta.png");
// });

// frenteTwVerm.addEventListener("click", function(){
//     frenteFan22Preta.setAttribute("src", "../img/frente/frente tw/frente tw Verm.png");
// });

/*-----------------------------------*/
/*Frente Twister*/

$('#frenteTw').hide();

$('#frenteTw22').click(function(){
    $('#frenteTw').show();
    $('#frente').hide();
});

$('#voltarFrenteTW').click(function(){
    $('#frente').show();
    $('#frenteTw').hide();
});

/*-----------------------------------*/
/*escapamento*/

$('#escap').hide();

$('#btEscap').click(function(){
    $('#escap').show();
    $('#selecPecas').hide();
});

$('#voltarEscap').click(function(){
    $('#selecPecas').show();
    $('#escap').hide();
});

/*escapamento*/
// const escapeDeLata = document.querySelector("#escapeDeLata");
// const escapeDeLataProt = document.querySelector("#escapeDeLataProt");
// const escapeTorbal = document.querySelector("#escapeTorbal");
// const escapeDoreAzulAT = document.querySelector("#escapeDoreAzulAT");
// const escapeDoreVermAT = document.querySelector("#escapeDoreVermAT");
// const escapeDorePretoAT = document.querySelector("#escapeDorePretoAT");
// const escapeDorePolidoAT = document.querySelector("#escapeDorePolidoAT");
// const escapeOrigPrata = document.querySelector("#escapeOrigPrata");
// const escapeOrigprata = document.querySelector("#escapeOrigprata");

// escapeOrigprata.addEventListener("click", function(){
//     escapeOrigPrata.setAttribute("src", "../img/escapamento/original/escapOrigPrata.png");
// });

// escapeDeLata.addEventListener("click", function(){
//     escapeOrigPrata.setAttribute("src", "../img/escapamento/delata/escapDeLata.png");
// });

// escapeDeLataProt.addEventListener("click", function(){
//     escapeOrigPrata.setAttribute("src", "../img/escapamento/delata/escapDeLataProt.png");
// });

// escapeTorbal.addEventListener("click", function(){
//     escapeOrigPrata.setAttribute("src", "../img/escapamento/delata/escapTorbalEstra.png");
// });

// escapeDoreAzulAT.addEventListener("click", function(){
//     escapeOrigPrata.setAttribute("src", "../img/escapamento/dore/escapDoreAzulAT.png");
// });

// escapeDoreVermAT.addEventListener("click", function(){
//     escapeOrigPrata.setAttribute("src", "../img/escapamento/dore/escapDoreVermAT.png");
// });

// escapeDorePretoAT.addEventListener("click", function(){
//     escapeOrigPrata.setAttribute("src", "../img/escapamento/dore/escapDorePretoAT.png");
// });

// escapeDorePolidoAT.addEventListener("click", function(){
//     escapeOrigPrata.setAttribute("src", "../img/escapamento/dore/escapDorePolidoAT.png");
// });

/*-----------------------------------*/
/*Rabeta*/
$('#rabeta').hide();

$('#btRabeta').click(function(){
    $('#rabeta').show();
    $('#selecPecas').hide();
});

$('#voltarRabeta').click(function(){
    $('#selecPecas').show();
    $('#rabeta').hide();
});

/*rabeta*/
// const rabetaOrig01 = document.querySelector("#rabetaOrig01");
// const rabetaorig01 = document.querySelector("#rabetaorig01");
// const rabetaOrig02 = document.querySelector("#rabetaOrig02");
// const rabetaOrig03 = document.querySelector("#rabetaOrig03");
// const rabetaOrig04 = document.querySelector("#rabetaOrig04");
// const rabetaOrig05 = document.querySelector("#rabetaOrig05");
// const rabetaOrig06 = document.querySelector("#rabetaOrig06");
// const rabetaNvI01 = document.querySelector("#rabetaNvI01");
// const rabetaNvI02 = document.querySelector("#rabetaNvI02");
// const rabetaNvI03 = document.querySelector("#rabetaNvI03");
// const rabetaNvII01 = document.querySelector("#rabetaNvII01");
// const rabetaNvII02 = document.querySelector("#rabetaNvII02");
// const rabetaNvII03 = document.querySelector("#rabetaNvII03");
// const rabetaNvII04 = document.querySelector("#rabetaNvII04");
// const rabetaNvII05 = document.querySelector("#rabetaNvII05");
// const rabetaNvIII01 = document.querySelector("#rabetaNvIII01");
// const rabetaNvIII02 = document.querySelector("#rabetaNvIII02");
// const rabetaNvIII03 = document.querySelector("#rabetaNvIII03");


// rabetaorig01.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaOrig01.png");
// });

// rabetaOrig02.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaOrig02.png");
// });

// rabetaOrig03.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaOrig03.png");
// });

// rabetaOrig04.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaOrig04.png");
// });

// rabetaOrig05.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaOrig05.png");
// });

// rabetaOrig06.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaOrig06.png");
// });

// rabetaNvI01.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaNvI01.png");
// });

// rabetaNvI02.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaNvI02.png");
// });

// rabetaNvI03.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaNvI03.png");
// });

// rabetaNvII01.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaNvII01.png");
// });

// rabetaNvII02.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaNvII02.png");
// });

// rabetaNvII03.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaNvII03.png");
// });

// rabetaNvII04.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaNvII04.png");
// });

// rabetaNvII05.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaNvII05.png");
// });

// rabetaNvIII01.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaNvIII01.png");
// });

// rabetaNvIII02.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaNvIII02.png");
// });

// rabetaNvIII03.addEventListener("click", function(){
//     rabetaOrig01.setAttribute("src", "../img/rabeta/rabetaNvIII03.png");
// })

/*alça*/
// const alcaOrigCromo = document.querySelector("#alcaOrigCromo");
// const alcaOrigPreta = document.querySelector("#alcaOrigPreta");
// const alcaOrigpreta = document.querySelector("#alcaOrigpreta");
// const alcaAltaCromo = document.querySelector("#alcaAltaCromo");
// const alcaAltaPreta = document.querySelector("#alcaAltaPreta");
// const alcaTitanPreta = document.querySelector("#alcaTitanPreta");
// const alcaTitanPrata = document.querySelector("#alcaTitanPrata");
// const churrasqueiraCromo = document.querySelector("#churrasqueiraCromo");
// const churrasqueiraCromoGivi = document.querySelector("#churrasqueiraCromoGivi");
// const churrasqueiraCromoGiviBau = document.querySelector("#churrasqueiraCromoGiviBau");
// const churrasqueiraCromoSup = document.querySelector("#churrasqueiraCromoSup");
// const churrasqueiraCromoSupBau = document.querySelector("#churrasqueiraCromoSupBau");
// const churrasqueiraPreta = document.querySelector("#churrasqueiraPreta");
// const churrasqueiraPretaGivi = document.querySelector("#churrasqueiraPretaGivi");
// const churrasqueiraPretaGiviBau = document.querySelector("#churrasqueiraPretaGiviBau");
// const churrasqueiraPretaSup = document.querySelector("#churrasqueiraPretaSup");
// const churrasqueiraPretaSupBau = document.querySelector("#churrasqueiraPretaSupBau");



// alcaOrigCromo.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/alcaOrigCromo.png");
// });

// alcaOrigpreta.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/alcaOrigPreta.png");
// });

// alcaAltaCromo.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/alcaAltaCromo.png");
// });

// alcaAltaPreta.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/alcaAltaPreta.png");
// });

// alcaTitanPreta.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/alcaTitanPreta.png");
// });

// alcaTitanPrata.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/alcaTitanPrata.png");
// });

// churrasqueiraCromo.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/churrasqueiraCromo.png");
// });

// churrasqueiraCromoGivi.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/churrasqueiraCromoGivi.png");
// });

// churrasqueiraCromoGiviBau.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/churrasqueiraCromoGiviBau.png");
// });

// churrasqueiraCromoSup.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/churrasqueiraCromoSup.png");
// });

// churrasqueiraCromoSupBau.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/churrasqueiraCromoSupBau.png");
// });

// churrasqueiraPreta.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/churrasqueiraPreta.png");
// });

// churrasqueiraPretaGivi.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/churrasqueiraPretaGivi.png");
// });

// churrasqueiraPretaGiviBau.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/churrasqueiraPretaGiviBau.png");
// });

// churrasqueiraPretaSup.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/churrasqueiraPretaSup.png");
// });

// churrasqueiraPretaSupBau.addEventListener("click", function(){
//     alcaOrigPreta.setAttribute("src", "../img/alca/churrasqueiraPretaSupBau.png");
// });

/*-----------------------------------*/
/*alça*/

$('#alca').hide();

$('#btAlca').click(function(){
    $('#alca').show();
    $('#selecPecas').hide();
});

$('#voltarAlca').click(function(){
    $('#selecPecas').show();
    $('#alca').hide();
});

/*-----------------------------------*/
/*tampa motor*/

$('#tampaMotor').hide();

$('#btTampaMotor').click(function(){
    $('#tampaMotor').show();
    $('#selecPecas').hide();
});

$('#voltarTampaMotor').click(function(){
    $('#selecPecas').show();
    $('#tampaMotor').hide();
});


/*motor*/
// const tampaPrata = document.querySelector("#tampaPrata");
// const tampaprata = document.querySelector("#tampaprata");
// const tampaPreta = document.querySelector("#tampaPreta");


// tampaprata.addEventListener("click", function(){
//     tampaPrata.setAttribute("src", "../img/vazio.png");
// });

// tampaPreta.addEventListener("click", function(){
//     tampaPrata.setAttribute("src", "../img/motor/tampaLateral/TampaPretaMotor.png");
// });

function mudarnome(){
    $("nomeProjeto").trigger( "submit" );
    
}