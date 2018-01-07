# -*- coding: utf-8 -*-
N = input()
media = []
for x in range (0,N):
    li = raw_input().split()

    a =  float(li[0])*2
    b =  float(li[1])*3
    c =  float(li[2])*5

    media.append((a+b+c)/10)

for x in range (0,N):
    print ("%0.1f"% media[x])
