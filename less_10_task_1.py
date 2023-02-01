import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяем переменную величину
t = np.arange(-5, 5, 0.1)


def diff_func(c, t):
    y, z = c
	
    # Первое уравнение системы
    dy_dx = y**2 * z
    # Второе уравнение системы
    dz_dx = z / t - y * z**2
    
    return dy_dx, dz_dx


y_0 = 1
z_0 = -3

c_0 = y_0, z_0

# Решаем систему диф. уравнений
solvers = odeint(diff_func, c_0, t)
# Строим решение в виде графика
plt.plot(t, solvers[:, 1])

# theta(omega)
# plt.plot(sol[:, 1], sol[:, 0], 'g', label='theta(omega)')

plt.savefig("task1")