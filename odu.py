import matplotlib
import math


x0=1
xk=7
y0=0.65
eps=0.001
y=[]

def fn1(x,y):
    return(x*math.sin(pow(x,2)*y/(x-y)))

