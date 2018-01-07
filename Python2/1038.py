# -*- coding: utf-8 -*-

linha = raw_input().split()
cod = int(linha[0])
qte = int(linha[1])

lista = [0,4.00,4.50,5.00,2.00,1.50]

print("Total: R$ %.2f" % (qte*lista[cod]))
