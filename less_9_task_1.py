import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.1)

def factory(n, t):
    dn_dt = n * -k
    
    return dn_dt

plt.grid()
plt.xlabel('time, годы')
n_0 = 1000
k = 0.08


n_t = odeint(factory, n_0, t)
	
plt.plot(t, n_t[:,0])
plt.savefig('invest.png')
