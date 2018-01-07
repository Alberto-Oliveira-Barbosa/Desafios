# -*- coding: utf-8 -*-

dias = int(input())
ano = dias / 365
meses = (dias - (ano * 365)) /30
dias = dias - ((ano *365) + (meses * 30))

print("%i ano(s)" % ano)
print("%i mes(es)" % meses)
print("%i dia(s)" % dias)
