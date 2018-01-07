# -*- coding: utf-8 -*-
N = (input())
if N >= 0 and N <= 1000000.00:
    total = 0
    dinheiro = [100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01]
    tipo = "nota(s)"
    print "NOTAS:"
    for i in range(0,12):
        total = N / dinheiro[i]
        N =  round(N % dinheiro[i],2)
        if i == 6:
            print"MOEDAS:"
            tipo = "moeda(s)"
        print("%i %s de R$ %.2f" % (total,tipo,dinheiro[i]))
