import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from constants import G

seconds_in_year = 365 * 24 * 60 * 60
seconds_in_day = 24 * 60 * 60

years = 75
frames = 365
t = np.linspace(0, years * seconds_in_year, frames)

# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3) = s

    # Динамика первого тела под влиянием второго и третьего
    dxdt1 = v_x1
    dv_xdt1 = (
      	    - G * m2 * (x1 - x2) 
               / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
            - G * m3 * (x1 - x3) 
               / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
              )
    dydt1 = v_y1
    dv_ydt1 = (
      	    - G * m2 * (y1 - y2) 
               / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
            - G * m2 * (y1 - y3) 
               / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
    	      )

    # Динамика второго тела под влиянием первого и третьего
    dxdt2 = v_x2
    dv_xdt2 = (
      	    - G * m1 * (x2 - x1) 
               / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
            - G * m3 * (x2 - x3) 
               / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
    	      )
    dydt2 = v_y2
    dv_ydt2 = (
      	    - G * m1 * (y2 - y1) 
               / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
            - G * m3 * (y2 - y3) 
               / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
              )

    # Динамика третьего тела под влиянием второго и первого
    dxdt3 = v_x3
    dv_xdt3 = (
      	    - G * m1 * (x3 - x1) 
               / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
            - G * m2 * (x3 - x2) 
               / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
              )
    dydt3 = v_y3
    dv_ydt3 = (
      	    - G * m1 * (y3 - y1) 
               / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
            - G * m2 * (y3 - y2) 
               / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
              )

    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3)

# Определяем начальные значения и параметры, 
# входящие в систему диф. уравнений
ae = 149 * 10**9
M = 2 * 10**(30)

m1 = 1.06 * M

m2 = 0.96 * M

m3 = 0.67 * M

x10 = 0
v_x10 = -8638
y10 = ae
v_y10 = 0

x20 = -12.3 * ae
v_x20 = 0
y20 = 0
v_y20 = -6638

x30 = 12.3 * ae
v_x30 = 0
y30 = 0
v_y30 = 4638

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30)


# Решаем систему диф. уравнений
sol = odeint(move_func, s0, t)

# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

balls = []
balls_lines = []

for i in range(3):
    balls.append(plt.plot([], [], 'o', color='r'))
    balls_lines.append(plt.plot([], [], '-', color='r'))

def animate(i):
    for j in range(3):
        balls[j][0].set_data(sol[i, 4*j], sol[i, 4*j+2])
        balls_lines[j][0].set_data(sol[:i, 4*j], sol[:i, 4*j+2])

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 5 * x30
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('task_1.gif')