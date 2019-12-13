#using scipy.interpolate.UnivariateSpline

import matplotlib.pyplot as pl
from scipy.interpolate import lagrange
from scipy.interpolate import CubicSpline
from scipy.interpolate import UnivariateSpline
from scipy import interpolate
from numpy.polynomial.polynomial import Polynomial
import numpy as np
x=[0,1,2,3,4,5]
y=[1.0,2.0,1.0,0.5,4.0,8.0]
pl.plot(x,y,'b.')
xs=np.linspace(0,5,100)
spl=UnivariateSpline(x,y,k=1)    
spl2=UnivariateSpline(x,y,k=2)
spl3=UnivariateSpline(x,y,k=3)
pl.plot(xs,spl(xs), 'g',label='linear fit')
pl.plot(xs,spl2(xs), 'b',label='quadratic fit')
pl.plot(xs,spl3(xs), 'r',label='cubic  fit')
poly=lagrange(x,y)       #scipy.interpolate.lagrange   (in orange colour)
pl.plot(xs,poly(xs),'--r',label='lagrange fit')
pl.legend()
pl.show()











spl2=UnivariateSpline(x,y,k=2)
pl.plot(xs,spl2(xs),'r')
cs=CubicSpline(x,y)       #cubic spline in dotted line
pl.plot(xs,cs(xs), '--r',label="c3")


poly=lagrange(x,y)       #scipy.integrate.lagrange   (in orange colour)
pl.plot(xs,poly(xs))

x1=np.array([0,1,2,3,4,5])
y1=np.array([1.0,2.0,1.0,0.5,4.0,8.0])
h=interpolate.interp1d(x1,y1)
xnew=np.linspace(0,5,100)
ynew=h(xnew)
 # quadratic spline


