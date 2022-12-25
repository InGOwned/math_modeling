import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
trajectory, = plt.plot([], [], '-', color='b')
ball, = plt.plot([], [], 'o', color='r')

plt.axis('equal')
plt.grid()

frames = np.arange(0, np.pi * 2.01, 0.045)

edge = 10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


def ellipse(p, e, fi):
    # fi = np.arange(0, np.pi * 8, 0.1)
    r = p / (1 + (e * np.cos(fi)))
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y


X, Y =[], []


def animate(i):
    X.append(ellipse(p = 3, e = 0.65, fi = i)[0])
    Y.append(ellipse(p = 3, e = 0.65, fi = i)[1])
    ball.set_data(ellipse(p = 3, e = 0.65, fi = i))
    trajectory.set_data(X, Y)
    plt.plot(-3.5, 0)
    return ball,


ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save("ellipse.gif")
