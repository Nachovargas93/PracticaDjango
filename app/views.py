# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render

# Create your views here.

def index(request):
    distritos = Distrito.objects.all()
    return render(request, 'index.html', {'listadistritos': distritos })

def ver_candidatos(request, id_candidatos):
    distrito_elegido = Distrito.objects.get(id= id_candidatos)
    candidatos = Candidato.objects.filter(distrito = distrito_elegido)
    return render(request, 'ver_candidatos.html', {'dic_distritos': distrito_elegido, 'dic_candidato': candidatos})

def ver_votos(request, id_votos):
    candidato_elegido = Candidato.objects.get(id=id_votos)
    votos = Voto.objects.filter(candidato = candidato_elegido)
    return render(request, 'ver_votos.html', {'dic_can': candidato_elegido, 'dic_votos': votos})