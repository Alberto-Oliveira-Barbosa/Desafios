# -*- coding: utf-8 -*-
salario = float(input())
imposto = 0.0
diferenca = 0.0

if salario>4500 :
    imposto = (1000.00 * 0.08) + (1500.00 * 0.18)
    diferenca = salario - 4500.00
    imposto += (diferenca*0.28)
    print("R$ %.2f"% imposto)

elif salario > 3000:
    imposto = 1000.00*0.08
    diferenca = salario - 3000.00
    imposto+= (diferenca *0.18)
    print("R$ %.2f" % imposto)

elif salario>2000:
    diferenca =salario - 2000.00
    imposto = diferenca * 0.08
    print("R$ %.2f" % imposto)
else:
    print"Isento"
