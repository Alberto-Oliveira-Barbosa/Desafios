# -*- coding: utf-8 -*-
y = input()

for x in range(0,y):
    N=int(input())

    if N%2==0 and N>0:
        print"EVEN POSITIVE"

    elif N%2==0 and N<0:
        print"EVEN NEGATIVE"

    elif N%2!=0 and N>0:
        print"ODD POSITIVE"

    elif N%2!=0 and N<0:
        print"ODD NEGATIVE"
    else:
        print"NULL"
