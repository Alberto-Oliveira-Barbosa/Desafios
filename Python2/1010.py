# -*- coding: utf-8 -*-

linha1 = raw_input().split()
linha2 = raw_input().split()

cod1 = int(linha1[0])
qtde1 = int(linha1[1])
valor1 = float(linha1[2])
cod2 = int(linha2[0])
qtde2 = int(linha2[1])
valor2 = float(linha2[2])

total = (qtde1 * valor1) + (qtde2 * valor2)

print("VALOR A PAGAR: R$ %0.2f" %total)
