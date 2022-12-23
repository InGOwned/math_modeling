import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
figure, = plt.plot([], [], '-', color='r')
plt.axis('equal')

# fi = np.arange(0, np.pi * 8, 0.1)


def ellipse(p, e):
    r = p / (1 + (e * np.cos(e)))

    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y


def animate(i):
    figure.set_data(ellipse(p = 3, e = 0.65))
    return figure,


ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)


ani = FuncAnimation(fig, animate, frames=np.arange(0, np.pi * 8, 0.1), interval=300)
ani.save("ellipse.gif")
