# -*- coding: utf-8 -*-
par=0
impar=0
negativo=0
positivo=0

for x in range(0,5):
    N=int(input())

    if N%2==0:
        par+=1

    else:
        impar+=1

    if N<0:
        negativo+=1

    elif N>0:
        positivo+=1



print ("%d valor(es) par(es)" %par)
print ("%d valor(es) impar(es)" %impar)
print ("%d valor(es) positivo(s)" %positivo)
print ("%d valor(es) negativo(s)" %negativo)
