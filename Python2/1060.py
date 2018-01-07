# -*- coding: utf-8 -*-
def testa_positivo(x):
    if x<0:
        return 0

    elif x>0:
        return 1

n = 0

positivo=0

for x in range(0,6):
    n = input()
    positivo+= testa_positivo(n)

print "%i valores positivos" % positivo
