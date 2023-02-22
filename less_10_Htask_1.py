import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяем переменную величину
t = np.arange(-1, 1, 0.01)


# Определяем функцию для системы диф. уравнений
def diff_func(c, t): # v - изменяемая величина для системы
    x, y, z = c # Указание изменяемых функций, через z
	
    # Первое уравнение системы
    dx_dt = 3 * x - y + z
    # Второе уравнение системы
    dy_dt = x + y + z
    # Третье уравнение системы
    dz_dt = 4 * x - y + 4 * z
    
    return dx_dt, dy_dt, dz_dt


# Определяем начальные значения и параметры,
# входящие в систему диф. уравнений
x_0 = -71
y_0 = 1
z_0 = -3

# Начальное значение изменяемой величины системы
c_0 = x_0, y_0, z_0

# Решаем систему диф. уравнений
solvers = odeint(diff_func, c_0, t)
# Строим решение в виде графика
plt.plot(t, solvers[:, 0], t, solvers[:, 1], t, solvers[:, 2])

plt.savefig("Htask1")