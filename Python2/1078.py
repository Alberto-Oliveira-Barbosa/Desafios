# -*- coding: utf-8 -*-

N = input()

if 2<N<1000:

    for x in range(1,11):

        print("%d x %d = %d"% (x, N, x*N))
