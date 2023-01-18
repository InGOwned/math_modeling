import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 100, 1)

def dot(v, t):
    dv_dt = g - k/m * v 
    return dv_dt

plt.grid()
plt.xlabel('time, с')

v_0 = 10
k = 0.5
m = 70
g = 9.8

v_t = odeint(dot, v_0, t)
	
plt.plot(t, v_t[:,0])
plt.savefig('force.png')
