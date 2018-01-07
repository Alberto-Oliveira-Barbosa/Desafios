# -*- coding: utf-8 -*-

x = int(input())
total_notas = 0
cedulas = [100,50,20,10,5,2,1]
print x
for i in range(0,7):
    total_notas = x / cedulas[i]
    x %= cedulas[i]
    print("%i nota(s) de R$ %i,00" % (total_notas,cedulas[i]))
