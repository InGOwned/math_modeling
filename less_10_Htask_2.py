import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяем переменную величину
t = np.arange(0, 5, 0.01)


def diff_func(c, t): 
    y, z = c 

    dy_dx = z

    dz_dx = (z**2 - 3 * (y**2)/(x**(1/2))) / y
    
    return dy_dx, dz_dx
y_0 = 0
z_0 = 1

c_0 = y_0, z_0

solvers = odeint(diff_func, c_0, t)

plt.plot(t, solvers[:, 0])

plt.savefig("Htask2")