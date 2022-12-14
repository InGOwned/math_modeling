from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
 
fig, ax = plt.subplots()
frakt, = plt.plot([], [], 'o', color='r')

plt.axis('equal')

x = []
y = []

x0 = 0.1
y0 = 0.1
C = 0.3
D = 0.33
# def mn(x0, y0, C, D):
for i in range(100):
    xn = x0**2 - y0**2 + C
    yn = 2 * x0 * y0 + D
    x.append(xn)
    y.append(yn)
    x0 = xn
    y0 = yn
    # return x, y


ax.set_xlim(-0.4, 0.5)
ax.set_ylim(0.2, 0.8)


def animate(i):
    frakt.set_data(x[:i], y[:i])

ani = FuncAnimation(fig, animate, frames=100, interval=100)

ani.save("Fraktal.gif")
