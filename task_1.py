import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from constants import G

seconds_in_year = 365 * 24 * 60 * 60
years = 8

frames = 365
t = np.linspace(0, years*seconds_in_year, frames)

def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4,
     x5, v_x5, y5, v_y5) = s

    dxdt1 = v_x1
    dv_xdt1 = - G * m * x1 / (x1**2 + y1**2)**1.5
    dydt1 = v_y1
    dv_ydt1 = - G * m * y1 / (x1**2 + y1**2)**1.5

    dxdt2 = v_x2
    dv_xdt2 = - G * m * x2 / (x2**2 + y2**2)**1.5
    dydt2 = v_y2
    dv_ydt2 = - G * m * y2 / (x2**2 + y2**2)**1.5

    dxdt3 = v_x3
    dv_xdt3 = - G * m * x3 / (x3**2 + y3**2)**1.5
    dydt3 = v_y3
    dv_ydt3 = - G * m * y3 / (x3**2 + y3**2)**1.5

    dxdt4 = v_x4
    dv_xdt4 = - G * m * x4 / (x4**2 + y4**2)**1.5
    dydt4 = v_y4
    dv_ydt4 = - G * m * y4 / (x4**2 + y4**2)**1.5

    dxdt5 = v_x5
    dv_xdt5 = - G * m * y5 / (x5**2 + y5**2)**1.5
    dydt5 = v_y5
    dv_ydt5 = - G * m * y5 / (x5**2 + y5**2)**1.5

    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4,
            dxdt5, dv_xdt5, dydt5, dv_ydt5)

m = 1.98 * 10**(30)
a = 1.27114 * 149 * 10**9
V_q = (G * m * (2 / (0.1399 * 149 * 10**9) - 1 / a))**0.5

x0_earth = 149 * 10**9
v_x0_earth = 0
y0_earth = 0
v_y0_earth = 30000

x0_mercury = 0
v_x0_mercury = -47360
y0_mercury = 0.38709927 * 149 * 10**9
v_y0_mercury = 0

x0_venus = -0.723332 * 149 * 10**9
v_x0_venus = 0
y0_venus = 0
v_y0_venus = -35020

x0_mars = 0
v_x0_mars = -24077
y0_mars = 1.523662 * 149 * 10**9
v_y0_mars = 0

x0_faethon = 0.1399 * 149 * 10**9
v_x0_faethon = 0
y0_faethon = 0
v_y0_faethon = V_q

s0 = (x0_earth, v_x0_earth, y0_earth, v_y0_earth,
      x0_mercury, v_x0_mercury, y0_mercury, v_y0_mercury,
      x0_venus, v_x0_venus, y0_venus, v_y0_venus,
      x0_mars, v_x0_mars, y0_mars, v_y0_mars,
      x0_faethon, v_x0_faethon, y0_faethon, v_y0_faethon)

# Решаем систему диф. уравнений
def solve_func(i, key):
    sol = odeint(move_func, s0, t)
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
        x2 = sol[i, 4]
        y2 = sol[i, 6]
        x3 = sol[i, 8]
        y3 = sol[i, 10]
        x4 = sol[i, 12]
        y4 = sol[i, 14]
        x5 = sol[i, 16]
        y5 = sol[i, 18]
    else:
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]
        x2 = sol[:i, 4]
        y2 = sol[:i, 6]
        x3 = sol[:i, 8]
        y3 = sol[:i, 10]
        x4 = sol[:i, 12]
        y4 = sol[:i, 14]
        x5 = sol[:i, 16]
        y5 = sol[:i, 18]
    return ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5))

# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='b')
ball_line1, = plt.plot([], [], '-', color='b')

ball2, = plt.plot([], [], 'o', color='r')
ball_line2, = plt.plot([], [], '-', color='r')

ball3, = plt.plot([], [], 'o', color='g')
ball_line3, = plt.plot([], [], '-', color='g')

ball4, = plt.plot([], [], 'o', color='cyan')
ball_line4, = plt.plot([], [], '-', color='cyan')

ball5, = plt.plot([], [], 'o', color='magenta')
ball_line5, = plt.plot([], [], '-', color='magenta')

plt.plot([0], [0], 'o', color='y', ms=20)

def animate(i):
    ball1.set_data(solve_func(i, 'point')[0])
    ball_line1.set_data(solve_func(i, 'line')[0])

    ball2.set_data(solve_func(i, 'point')[1])
    ball_line2.set_data(solve_func(i, 'line')[1])

    ball3.set_data(solve_func(i, 'point')[2])
    ball_line3.set_data(solve_func(i, 'line')[2])

    ball4.set_data(solve_func(i, 'point')[3])
    ball_line4.set_data(solve_func(i, 'line')[3])

    ball5.set_data(solve_func(i, 'point')[4])
    ball_line5.set_data(solve_func(i, 'line')[4])

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')

edge = 4 * x0_earth
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('earth_mercury_venus_mars_sun_TEST.gif')