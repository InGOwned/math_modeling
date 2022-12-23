import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
square_fig, = plt.plot([], [], '-', color='r')

a = 1


def square_func():
    x = np.array([a, a, -a, -a, a])
    y = np.array([a, -a, -a, a, a])
    return x, y


def animate(i):
    x, y = square_func()
    X = x * np.cos(i) - y * np.sin(i)
    Y = y * np.cos(i) + x * np.sin(i)
    
    square_fig.set_data(X, Y)
    
    return square_fig

edge = 2
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
plt.axis('equal')

ani = FuncAnimation(fig, animate, frames=np.arange(0, 2 * np.pi, 0.01), interval=30)

ani.save('square.gif')
