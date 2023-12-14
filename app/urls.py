from tracemalloc import start
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('escolherMoto', views.escolherMoto, name='escolherMoto'),
    path('start/<int:id>', views.start, name='start'),
    path('sobre', views.sobre, name='sobre'),
    path('garagem/', views.garagem, name='garagem'),
    path('novo', views.novo, name='novo'),
    path('edit/moto/<int:id>/roda_d/<int:valor>', views.mudar_roda_d, name='edit_roda_d'),
    path('edit/moto/<int:id>/roda_t/<int:valor>', views.mudar_roda_t, name='edit_roda_t'),
    path('edit/moto/<int:id>/tanque/<int:valor>', views.mudar_tanque, name='edit_tanque'),
    path('edit/moto/<int:id>/carenagemTraseira/<int:valor>', views.mudar_carenagemTraseira, name='edit_carenagemTraseira'),
    path('edit/moto/<int:id>/frente/<int:valor>', views.mudar_frente, name='edit_frente'),
    path('edit/moto/<int:id>/escapamento/<int:valor>', views.mudar_escapamento, name='edit_escapamento'),
    path('edit/moto/<int:id>/rabeta/<int:valor>', views.mudar_rabeta, name='edit_rabeta'),
    path('edit/moto/<int:id>/alca/<int:valor>', views.mudar_alca, name='edit_alca'),
    path('edit/moto/<int:id>/tampaMotor/<int:valor>', views.mudar_tampaMotor, name='edit_tampaMotor'),
]