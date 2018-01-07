# -*- coding: utf-8 -*-
linha = raw_input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])
AB = ((a+b+abs(a-b))/2)
ABC = ((AB + c + abs(AB - c))/2)
print("%i eh o maior" % ABC)
