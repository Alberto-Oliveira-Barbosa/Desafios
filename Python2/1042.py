# -*- coding: utf-8 -*-

linha = raw_input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])
aux = [a,b,c]
aux.sort()
for i in range(0,3):
    print(aux[i])
print ("")
for i in range(0,3):
    print(linha[i])
