# -*- coding: utf-8 -*-
def testa_pares(x):
    if x%2==0:
        return 1

    else:
        return 0

n = 0

par=0

for x in range(0,5):
    n = input()
    par+= testa_pares(n)

print "%i valores pares" % par
