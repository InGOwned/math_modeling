import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
figure, = plt.plot([], [], '-', color='r')
plt.axis('equal')

frames = np.arange(0, np.pi * 8, 0.1)

edge = 20
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


def ellipse(p, e, fi):
    # fi = np.arange(0, np.pi * 8, 0.1)
    r = p / (1 + (e * np.cos(fi)))
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y


def animate(i):
    figure.set_data(ellipse(p = 3, e = 0.65, fi = i))
    return figure,


ani = FuncAnimation(fig, animate, frames=frames, interval=300)
ani.save("ellipse.gif")
