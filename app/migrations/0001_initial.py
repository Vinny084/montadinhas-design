# Generated by Django 4.1.5 on 2023-11-23 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roda_t', models.CharField(choices=[('static/img/roda/pe/traseira/preto.png', 'pe traseira'), ('static/img/roda/raiada/traseira.png', 'raiada traseira')], max_length=150, verbose_name='Roda Traseira')),
                ('roda_d', models.CharField(choices=[('static/img/roda/pe/dianteira/preto/preto.png', 'pe dianteira'), ('static/img/roda/raiada/dianteira.png', 'raiada diateira')], max_length=150, verbose_name='Roda Dianteira')),
                ('paralama', models.CharField(choices=[('static/img/roda/pe/dianteira/preto/preto.png', 'pe preto'), ('static/img/roda/pe/dianteira/preto/vermelho.png', 'pe vermelho'), ('static/img/roda/raiada/dianteira.png', 'raiada preto'), ('static/img/roda/raiada/paralama/vermelha.png', 'raiada vermelho')], max_length=150)),
                ('rabeta', models.CharField(choices=[('static/img/rabeta/rabetaOrig01.png', 'Orig01'), ('static/img/rabeta/rabetaOrig02.png', 'Orig02'), ('static/img/rabeta/rabetaOrig03.png', 'Orig03'), ('static/img/rabeta/rabetaOrig04.png', 'Orig04'), ('static/img/rabeta/rabetaOrig05.png', 'Orig05'), ('static/img/rabeta/rabetaOrig06.png', 'Orig06'), ('static/img/rabeta/rabetaNvI01.png', 'NvI01'), ('static/img/rabeta/rabetaNvI02.png', 'NvI02'), ('static/img/rabeta/rabetaNvI03.png', 'NvI03'), ('static/img/rabeta/rabetaNvII01.png', 'NvII01'), ('static/img/rabeta/rabetaNvII02.png', 'NvII02'), ('static/img/rabeta/rabetaNvII03.png', 'NvII03'), ('static/img/rabeta/rabetaNvII04.png', 'NvII04'), ('static/img/rabeta/rabetaNvII05.png', 'NvII05'), ('static/img/rabeta/rabetaNvIII01.png', 'NvIII01'), ('static/img/rabeta/rabetaNvIII02.png', 'NvII02'), ('static/img/rabeta/rabetaNvIII03.png', 'NvIII03')], max_length=150)),
                ('carenagemTraseira', models.CharField(choices=[('static/img/carenagem/traseira/carenagemTrasPreta.png', 'PRETO'), ('static/img/carenagem/traseira/carenagemTrasVerm.png', 'VERMELHO')], max_length=150)),
                ('frente', models.CharField(choices=[('static/img/frente/frente fan 22/frente fan 22 preta.png', 'Fan preta'), ('static/img/frente/frente fan 22/frente fan 22 verm.png', 'Fan vermelha'), ('static/img/frente/frente titan 22/frente titan 22 preta.png', 'Titan preta'), ('static/img/frente/frente titan 22/frente titan 22 verm.png', 'Titan vermelha'), ('static/img/frente/frente tw/frente tw preta.png', 'Twister preta'), ('static/img/frente/frente tw/frente tw verm.png', 'Twister vermelha')], max_length=150)),
                ('escapamento', models.CharField(choices=[('static/img/escapamento/original/escapOrigPrata.png', 'original'), ('static/img/escapamento/delata/escapDeLata.png', 'delata'), ('static/img/escapamento/delata/escapDeLataProt.png', 'delata com protecao'), ('static/img/escapamento/delata/escapTorbalEstra.png', 'torbal'), ('static/img/escapamento/dore/escapDoreAzulAT.png', 'dore azul'), ('static/img/escapamento/dore/escapDoreVermAT.png', 'dore vermelho'), ('static/img/escapamento/dore/escapDorePretoAT.png', 'dore preto'), ('static/img/escapamento/dore/escapDorePolidoAT.png', 'dore prata')], max_length=150)),
                ('tampaMotor', models.CharField(choices=[('static/img/vazio.png', 'prata'), ('static/img/motor/tampaLateral/tampaPretaMotor.png', 'preta')], max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Start',
            fields=[
                ('moto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.moto')),
            ],
            bases=('app.moto',),
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.moto')),
            ],
        ),
    ]
