#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt


def sphere(X, Y, Z, r, ax):
    Xtemp = []
    Ytemp = []
    Ztemp = []
    Xneg = []
    Yneg = []
    Zneg = []
    for x in X :
        for y in Y :
            for z in Z :
                sphere = math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2)
                if sphere < math.pow(r, 2):
                    Xtemp.append(x)
                    Ytemp.append(y)
                    Ztemp.append(z)
                    Xneg.append(-x)
                    Yneg.append(-y)
                    Zneg.append(-z)
                    
    ax.scatter(Xtemp, Ytemp, Ztemp, color = 'red')
    ax.scatter(Xtemp, Ytemp, Zneg, color = 'red')
    ax.scatter(Xtemp, Yneg, Ztemp, color = 'red')
    ax.scatter(Xtemp, Yneg, Zneg, color = 'red')
    
    ax.scatter(Xneg, Ytemp, Zneg, color = 'red')
    ax.scatter(Xneg, Ytemp, Ztemp, color = 'red')
    ax.scatter(Xneg, Yneg, Zneg, color = 'red')
    ax.scatter(Xneg, Yneg, Ztemp, color = 'red')
        


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')


X = []
Y = []
Z = []
r = 1

for i in range (0, 101) :
    X.append(i/100)
    Y.append(i/100)
    Z.append(i/100)


sphere(X, Y, Z, r, ax)


plt.show()
