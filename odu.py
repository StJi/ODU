import matplotlib.pyplot as plt
import math
import numpy as np


x0=1
xk=7
y0=0.65
eps=0.001
h=0.1
y=[]
x=[]

for i in np.arange(x0, xk + h, h):
    x.append(i)

def fn1(x,y):
    return(x*math.sin(pow(x,2)*y/(x-y)))

def eil(x0,xk,y0,h=0.1):
    y.append(y0)
    i=1
    for x in np.arange(x0+h,xk+h,h):

        y.append(y[i-1]+h*fn1(x,y[i-1]))
        i += 1;
    return y
def out(x,y):
    plt.plot(x,y)
    plt.show()

out(x,eil(x0,xk,y0,h))
