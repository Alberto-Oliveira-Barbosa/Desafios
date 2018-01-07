# -*- coding: utf-8 -*-
x = input()
lista = []
dentro = 0
fora = 0
for i in range(0,x):
    lista.append(input())
for i in range(0,x):
    if lista[i] >= 10 and lista[i]<=20:
        dentro+=1
    else:
        fora+=1

print "%i in" % dentro
print "%i out" % fora
