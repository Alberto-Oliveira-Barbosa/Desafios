# -*- coding: utf-8 -*-
N = input()

if(N < 10000):
    for x in range (1, 10000):
        if(x % N == 2):
            print x
