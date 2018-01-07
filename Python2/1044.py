# -*- coding: utf-8 -*-

n = raw_input().split()
x = int(n[0])
y = int(n[1])

if (x%y==0 or y%x==0):
    print"Sao Multiplos"
else:
    print"Nao sao Multiplos"
