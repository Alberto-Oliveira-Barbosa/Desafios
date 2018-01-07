# -*- coding: utf-8 -*-
li = raw_input().split()
a = float(li[0])
b = float(li[1])
c = float(li[2])
perim = 0.0
area = 0.0

if ((a+b)>c and (b+c)>a and (a+c)>b):
    perim = float(a+b+c)
    print("Perimetro = %.1f" % perim)
else:
    area = float(c*(a+b)/2.0)
    print("Area = %.1f" % area)
