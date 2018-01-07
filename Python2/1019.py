# -*- coding: utf-8 -*-
segundos = int(input())

horas = segundos / 3600
minutos = (segundos - (horas * 3600)) /60
segundos = segundos - ((horas * 3600) + (minutos * 60))

print ("%i:%i:%i" % (horas, minutos,segundos))
