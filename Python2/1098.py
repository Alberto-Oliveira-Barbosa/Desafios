# -*- coding: utf-8 -*-
i = 0.0
j = 0.0
for x in range(0,11):
    for z in range(1,4):
        if x%5 == 0:
            print("I=%.0f J=%.0f" % (i, j+z))
        else:
            print("I=%.1f J=%.1f" % (i, j+z))
    i+=0.2
    j+=0.2
    
