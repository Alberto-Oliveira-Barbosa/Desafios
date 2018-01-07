# -*- coding: utf-8 -*-
s = float(input())
rea = 0.0
perc = ""

if s <= 400:
    rea = (s * 15.0)/100
    perc = "15 %"
elif s >400 and s <=800:
    rea = (s * 12.0)/100
    perc = "12 %"
elif s> 800 and s <= 1200:
    rea = (s * 10.0)/100
    perc = "10 %"
elif s>1200 and s <= 2000:
    rea = (s * 7.0)/100
    perc = "7 %"
else:
    rea = (s * 4)/100
    perc = "4 %"

print"Novo salario: %.2f" % (s + rea)
print"Reajuste ganho: %.2f" % rea
print"Em percentual: %s" % perc
