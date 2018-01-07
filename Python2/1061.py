# -*- coding: utf-8 -*-
dias = raw_input().split()

di = int(dias[1])

dado = raw_input().split(':')
hi = int(dado[0])
mi = int(dado[1])
si = int(dado[2])

dias = raw_input().split()

df = int(dias[1])

dado = raw_input().split(':')

hf = int(dado[0])
mf = int(dado[1])
sf = int(dado[2])

dia = 0
hora = 0
minuto = 0
segundo = 0

dia = df - di

hora = hf - hi
if hora < 0:
    hora = 24 + hora
    dia -= 1

minuto = mf - mi
if minuto< 0:
    minuto = 60 + minuto
    hora -= 1

segundo = sf - si
if segundo < 0:
    segundo = 60 + segundo
    minuto -= 1

if dia  <0:
    dia = 0

print "%d dia(s)" % dia
print "%d hora(s)" % hora
print "%d minuto(s)" % minuto
print "%d segundo(s)" % segundo
