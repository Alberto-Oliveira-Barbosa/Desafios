# -*- coding: utf-8 -*-

n = raw_input().split()
lista = [float(n[0]),float(n[1]),float(n[2])]
lista.sort()
lista.reverse()

a = lista[0]
b = lista[1]
c = lista[2]



if (a>=(b+c)):
    print("NAO FORMA TRIANGULO")

else:

    if (a*a == ((b*b)+(c*c))):
        print("TRIANGULO RETANGULO")

    if (a*a > ((b*b) + (c*c))):
        print("TRIANGULO OBTUSANGULO")

    if (a*a < ((b*b) + (c*c))):
        print("TRIANGULO ACUTANGULO")

    if (a == b and b == c ):
        print("TRIANGULO EQUILATERO")

    elif (a == b or b == c):
        print("TRIANGULO ISOSCELES")
