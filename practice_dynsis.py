#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt

def rho (u, v) :
    global r0
    r0 = 1
    c = []
    for i in range (17) :
        c.append(1)
    theta = (math.atan(-c[15]*(v-c[16]))+1)/2
    return ((c[1]+(c[2]*math.exp(-((v-c[3])**2)/c[4])+c[5])*math.sin(u/r0)) + ((c[6]*math.exp(-((v-c[7])**2)/c[8])+c[9])*math.sin((2*u)/r0)) + ((c[10]*math.exp(-((v-c[11])**2)/c[12])+c[13])*math.sin((3*u)/r0)))*theta + (1/math.sqrt((math.cos(u/r0)**2/(c[1]**2))+(math.sin(v/r0)**2/(c[14]**2))))*(1-theta)



def r_vec (u, v) :
    if v < 0 :
        return rho(u, v)*math.cos(u/r0) , v , rho(u, v)*math.sin(u/r0)
    if v > 0 :
        return rho(u, v)*math.cos(u/r0)*math.cos(v/r0) , rho(u, v)*math.sin(v/r0) , rho(u, v)*math.sin(u/r0)*math.cos(v/r0)



    
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')



U = np.arange(-1.0, 1.0, 0.1)
V = np.arange(-1.0, 1.0, 0.1)

for u,v in zip(U, V) :
    print(u, v)


S = []
for u in U :
    for v in V :
        S.append(r_vec(u,v))


print(S)

ax.plot(S[0], S[1], S[2])


        



#def sphere(X, Y, Z, r, ax):
#    Xtemp = []
#    Ytemp = []
#    Ztemp = []
#    Xneg = []
#    Yneg = []
#    Zneg = []
#    for x in X :
#        for y in Y :
#            for z in Z :
#                sphere = math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2)
#                if sphere < math.pow(r, 2):
#                    Xtemp.append(x)
#                    Ytemp.append(y)
#                    Ztemp.append(z)
#                    Xneg.append(-x)
#                    Yneg.append(-y)
#                    Zneg.append(-z)
#                    
#    ax.scatter(Xtemp, Ytemp, Ztemp, color = 'red')
#    ax.scatter(Xtemp, Ytemp, Zneg, color = 'red')
#    ax.scatter(Xtemp, Yneg, Ztemp, color = 'red')
#    ax.scatter(Xtemp, Yneg, Zneg, color = 'red')
#    
#    ax.scatter(Xneg, Ytemp, Zneg, color = 'red')
#    ax.scatter(Xneg, Ytemp, Ztemp, color = 'red')
#    ax.scatter(Xneg, Yneg, Zneg, color = 'red')
#    ax.scatter(Xneg, Yneg, Ztemp, color = 'red')
        


#fig = plt.figure()
#ax = fig.add_subplot(111, projection = '3d')


#X = []
#Y = []
#Z = []
#r = 1
#
#for i in range (0, 101) :
#    X.append(i/100)
#    Y.append(i/100)
#    Z.append(i/100)
#
#
#sphere(X, Y, Z, r, ax)
#
#
plt.show()
