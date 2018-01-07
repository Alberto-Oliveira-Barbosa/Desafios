# -*- coding: utf-8 -*-
N = input()

if N>5 and N<2000:
    for x in range(1,N+1):
        if x%2 == 0:
            print ("%d^2 = %d"% (x, x*x))
