# -*- coding: utf-8 -*-
import sys

cobaias = { 'R' : 0,
            'S' : 0,
            'C' : 0 }

N = input()

for x in range(0, N):
    Quantia,Tipo = sys.stdin.readline().split()
    if(int(Quantia) >= 1 and int(Quantia) <= 15):
        cobaias[Tipo] += int(Quantia)

total = int(cobaias["C"]) + int(cobaias["R"]) + int(cobaias["S"])

print "Total:", total, "cobaias"
print "Total de coelhos:",cobaias["C"]
print "Total de ratos:",cobaias["R"]
print "Total de sapos:",cobaias["S"]

print "Percentual de coelhos: %.2f" % ((float(cobaias["C"]) * 100) / total), "%"
print "Percentual de ratos: %.2f" % ((float(cobaias["R"]) * 100) / total), "%"
print "Percentual de sapos: %.2f" % ((float(cobaias["S"]) * 100) / total), "%"
