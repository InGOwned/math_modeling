import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r')
plt.axis('equal')

frames = np.arange(0, np.pi * 8, 0.06)

edge = 10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


def ellipse(p, e, fi):
    # fi = np.arange(0, np.pi * 8, 0.1)
    r = p / (1 + (e * np.cos(fi)))
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y


def animate(i):
    ball.set_data(ellipse(p = 3, e = 0.65, fi = i))
    return ball,


ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save("ellipse.gif")
