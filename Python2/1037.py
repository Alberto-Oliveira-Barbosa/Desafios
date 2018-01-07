# -*- coding: utf-8 -*-

x = float(input())

msg = ""

if x >= 0 and x <=25:
    msg = "Intervalo [0,25]"
elif x > 25 and x <= 50:
    msg = "Intervalo (25,50]"
elif x >50 and x <= 75:
    msg = "Intervalo (50,75]"
elif x > 75 and x <= 100:
    msg = "Intervalo (75,100]"
else:
    msg = "Fora de intervalo"
print msg
