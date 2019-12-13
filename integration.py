#integration using composite trapezoidal rule
import numpy as np
x=np.linspace(0,1,100)
f=np.exp(x)

integrate=np.trapz(f,x)
print(integrate)


#integration by simpson rule
import scipy.integrate as sc
import numpy as np
def f(x):
    return np.exp(x)
x=np.linspace(0,1,100)
y=f(x)
integr=sc.simps(y,x)
print(integr)

#integration using romberg algorithm
import scipy.integrate as sc
import numpy as np
import scipy.special as sp
integ=sc.romberg(lambda x:np.exp(x),0,1)
print(integ)

#integration using fixed quad
inte=sc.fixed_quad(lambda x:np.exp(x),0,1,n=100)
print(inte)
