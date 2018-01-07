# -*- coding: utf-8 -*-

import math
linha1 = raw_input().split()
linha2 = raw_input().split()
x1 = float(linha1[0])
y1 = float(linha1[1])
x2 = float(linha2[0])
y2 = float(linha2[1])

dis = math.sqrt(((x2 - x1)**2) + ((y2-y1)**2))

print("%.4f" % dis)
