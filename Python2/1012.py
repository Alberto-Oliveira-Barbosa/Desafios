# -*- coding: utf-8 -*-
li = raw_input().split()
a = float(li[0])
b = float(li[1])
c = float(li[2])
pi = 3.14159

tri = a*c/2
cir = pi * c**2
tra =(c*(a+b))/2
qua = b**2
ret = a*b

print("TRIANGULO: %.3f" % tri)
print("CIRCULO: %.3f" % cir)
print("TRAPEZIO: %.3f" % tra)
print("QUADRADO: %.3f" % qua)
print("RETANGULO: %.3f" % ret)
