# -*- coding: utf-8 -*-
li = raw_input().split()
x = int(li[0])
y = int(li[1])
duracao = y - x


if duracao < 0:
    duracao += 24

if x == y:
    print "O JOGO DUROU 24 HORA(S)"
else:
    print"O JOGO DUROU %i HORA(S)" % duracao
