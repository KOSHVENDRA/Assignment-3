#finding root using bisection method

import math as m
from scipy import optimize
def f(x):
    return (m.sin(m.cos(m.exp(x))))
root=optimize.bisect(f,-1,1)
print('the root is using bisection method is :')
print (root)
print('the value of function at its root is:')
print(f(root))
  # now using newton-raphson method
def g(x):
    return((-1)*m.exp(x)*m.sin(m.exp(x))*m.cos(m.cos(m.exp(x))))
rootnew=optimize.newton(f,-1,fprime=g)
print('root using newton raphson method with initial point -1 is:')
print(rootnew)


rootnew2=optimize.newton(f,-0.1,fprime=g)
print('root using newton raphson method with initial point -0.1 is:')
print(rootnew2)


rootnew3=optimize.newton(f,-0.1)
print('finding root using secant method :')
print(rootnew3)
