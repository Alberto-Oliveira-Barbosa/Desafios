# -*- coding: utf-8 -*-
ddd = {61:"Brasilia",
       71:"Salvador",
       11:"Sao Paulo",
       21:"Rio de Janeiro",
       32: "Juiz de Fora",
       19: "Campinas",
       27:"Vitoria",
       31:"Belo Horizonte"}

n = input()
if (n in ddd):
    print ddd[n]
else:
    print"DDD nao cadastrado"
