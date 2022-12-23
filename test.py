import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
figure, = plt.plot([], [], '-', color='r')
plt.axis('equal')

fi = np.arange(0, np.pi * 8, 0.1)


def ellipse(p, e, fi):
    r = p / (1 + (e * np.cos(fi)))

    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y


def animate(i):
    figure.set_data(ellipse(p = 3, e = 0.65, fi = fi))
    return figure,

edge = 10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


ani = FuncAnimation(fig, animate, frames=500, interval=30)
ani.save("ellipse.gif")
