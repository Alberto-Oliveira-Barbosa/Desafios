# -*- coding: utf-8 -*-
n = input()
soma = 0
xy = []

for i in range(0,n):
    global soma
    global x
    global y
    li = raw_input().split()
    xy = [int(li[0]),int(li[1])]
    xy.sort()

    if xy[0] == xy[1]:
        soma = 0

    elif xy[0]%2 ==0:
        for i in range(xy[0]+1,xy[1],2):
            soma += int(i)

    else:
        for j in range(xy[0]+2,xy[1],2):
            soma += int(j)

    print soma
    soma = 0
