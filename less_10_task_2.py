import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяем переменную величину
t = np.arange(-1, 1, 0.1)


def diff_func(c, t):
    x, y = c
	
    # Первое уравнение системы
    dx_dt = 3 * x - 2 * y + (np.exp(3 * t) / (np.exp(t) + 1))
    # Второе уравнение системы
    dy_dt = x - (np.exp(3 * t / (np.exp(t) + 1)))
    
    return dx_dt, dy_dt


x_0 = 5
z_0 = -7

c_0 = x_0, z_0

# Решаем систему диф. уравнений
solvers = odeint(diff_func, c_0, t)
# Строим решение в виде графика
plt.plot(t, solvers[:, 0])

# theta(omega)
# plt.plot(sol[:, 1], sol[:, 0], 'g', label='theta(omega)')

plt.savefig("task2")