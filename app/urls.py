from tracemalloc import start
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('escolherMoto', views.escolherMoto, name='escolherMoto'),
    path('start/<int:id>', views.start, name='start'),
    path('sobre', views.sobre, name='sobre'),
    path('garagem/', views.garagem, name='garagem'),
    path('edit/moto/<int:id>/roda_d/<int:valor>', views.mudar_roda_d, name='edit_roda_d'),
]