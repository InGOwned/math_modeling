import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames=300
t = np.linspace(0, 5, frames)


def diff_func(c, t): 
    v_y, y0 = c 
    dy_dt = v_y
    dvy_dt = -g - u * v_y
    
    return dy_dt, dvy_dt

g = 9.8
v_y0 = 20
u = 0.1
y0 = 0



c_0 = v_y0, y0

# Решаем систему диф. уравнений
# def solve_func(i, key):
#     sol = odeint(move_func, c_0, t)
#     if key == 'point':
#         y = sol[i, 1]
#     else:
#         y = sol[:i, 2]
#     return y
  
# Строим решение в виде графика и анимируем
# fig, ax = plt.subplots()

# ball, = plt.plot([], [], 'o', color='r')
# ball_line, = plt.plot([], [], '-', color='r')

# def animate(i):
#     ball.set_data(solve_func(i, 'point'))
#     ball_line.set_data(solve_func(i, 'line'))

# ani = FuncAnimation(fig,
#                     animate,
#                     frames=frames,
#                     interval=30)

# edge = 15
# ax.set_xlim(0, edge)
# ax.set_ylim(0, edge)

# ani.save("task1.gif")


solvers = odeint(diff_func, c_0, t)

plt.plot(t, solvers[:, 0])

plt.savefig("task1_1")