# -*- coding: utf-8 -*-
n = raw_input().split()
x = float(n[0])
y = float(n[1])
msg = ""

if (x == 0 and y ==0):
    msg = "Origem"
elif(x==0 and y!=0):
    msg = "Eixo Y"
elif(x!=0 and y ==0):
    msg = "Eixo X"
elif (x>0 and y>0):
    msg = "Q1"
elif (x < 0 and y>0):
    msg = "Q2"
elif (x<0 and y<0):
    msg = "Q3"
else:
    msg = "Q4"

print msg
