import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяем переменную величину
t = np.arange(-5, 5, 0.1)


def diff_func(c, t):
    x, y = c
	
    # Первое уравнение системы
    dx_dt = y
    # Второе уравнение системы
    dy_dt = np.sin(t) + np.cos(t)
    
    return dx_dt, dy_dt


x_0 = 0
y_0 = 3

c_0 = x_0, y_0

# Решаем систему диф. уравнений
solvers = odeint(diff_func, c_0, t)
# Строим решение в виде графика
plt.plot(t, solvers[:, 0], solvers[:, 1])

plt.savefig("task3")