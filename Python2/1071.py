# -*- coding: utf-8 -*-
x = input()
y = input()
soma = 0

if x == y:
    soma = 0

elif x<y:
    if x%2 ==0:
        for i in range(x+1,y,2):
            soma += i

    else:
        for i in range(x+2,y,2):
            soma += i
else:
    if y%2 == 0:
        for i in range(y+1,x,2):
            soma += i
    else:
        for i in range(y+2,x,2):
            soma += i

print soma
