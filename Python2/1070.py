# -*- coding: utf-8 -*-

n = int(input())

if n%2==0:
    for x in range(n+1,n+12,2):
        print x
else:
    for x in range(n, n+12, 2):
        print x
