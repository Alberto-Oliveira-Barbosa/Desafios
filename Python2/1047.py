# -*- coding: utf-8 -*-
li = raw_input().split()
hi = int(li[0])
mi = int(li[1])
hf = int(li[2])
mf = int(li[3])
horas = hf - hi
minutos = mf - mi

if horas < 0:
    horas += 24

if minutos< 0:
    minutos+=60
    horas-=1

if hi == hf:
    horas = 24

print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" % (horas, minutos))
