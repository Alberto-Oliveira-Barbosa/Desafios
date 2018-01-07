# -*- coding: utf-8 -*-
lista = []
posicao = int(0)

for x in range(0,100):
    lista.append(int(input()))

for x in range(0,100):
    if lista[x] == max(lista):
        posicao = x

print max(lista)
print posicao+1
