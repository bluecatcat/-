#!/usr/bin/env python
# coding: utf-8



def beta(x,a,b,l,r):
    if x<l or x==l:
        return 0
    elif l<x and x<r:
        return C(x,l,a,b,r)/B(a,b)
    else:
        return 1



def func1(t,a,b,l,r):
    if t==l:
        return 0
    else:
        div = pow(t-l,a-1)*pow(r-t,b-1)
        dived = pow(r-l,a+b-1)
        return div/dived



def func2(u,a,b):
    return pow(u,a-1)*pow(1-u,b-1)



from scipy import integrate
def B(a,b):
    v,err = integrate.quad(func2,0,1,args=(a,b))
    return v
def C(x,a,b,l,r):
    v,err = integrate.quad(func1,l,x,args=(a,b,l,r))
    return v



import numpy as np
from matplotlib import pyplot as plt
x = np.arange(-0.1,0.1,0.01)
y = np.arange(-0.1,0.1,0.01)

for i,item in enumerate(x):
    y[i] = beta(item,2,2,0,0.02)

plt.plot(x,y)
plt.show()

