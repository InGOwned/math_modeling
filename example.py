import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames=300
t = np.linspace(0, 5, frames)


def move_func(c, t): 
    x, v_x, y, v_y = c 
	
    dx_dt = v_x
    dvx_dt = -4
    
    dy_dt = v_y
    dvy_dt = -g
    
    return dx_dt, dvx_dt, dy_dt, dvy_dt

g = 9.8
v = 15

alpha = 80 * np.pi / 180

x_0 = 0
v_x0 = v * np.cos(alpha)

y_0 = 0
v_y0 = v * np.sin(alpha)

c_0 = x_0, v_x0, y_0, v_y0

# Решаем систему диф. уравнений
def solve_func(i, key):
    sol = odeint(move_func, c_0, t)
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y
  
# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')

def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 15
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ani.save("example1.gif")
