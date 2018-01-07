# -*- coding: utf-8 -*-
n = 0
media = 0.0
positivo=0


def testa_positivo(x):
    if x<0:
        return 0

    elif x>0:
        global media
        media+=x
        return 1

for x in range(0,6):
    n = float(input())
    positivo+= testa_positivo(n)

media = media/positivo

print"%i valores positivos" % positivo
print "%.1f" % media
