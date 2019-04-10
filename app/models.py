# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Distrito(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Candidato(models.Model):
    nombre = models.CharField(max_length=30)
    distrito = models.ForeignKey(Distrito)

    def __str__(self):
        return 'Soy el candidato {} '.format(self.nombre)

class Voto(models.Model):
    candidato = models.ForeignKey(Candidato)
    valido = models.BooleanField(default=True)

    def __str__(self):
        return 'Votos: {}'.format(self.valido)




