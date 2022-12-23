import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='b')
trajectory, = plt.plot([], [], '-', color='b')
wells, = plt.plot([], [], '-', color='g')

frames = np.arange(0, 4.85 * np.pi, 0.06)
plt.axis('equal')

ax.set_xlim(-2, 15)
ax.set_ylim(0, 10)


def cicloida(R, t):
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    return x, y

def weels_func(R, x0, y0, xv0, yv0, t):
    x0 = x0 + xv0 * t
    y0 = y0 + yv0 * t

    alpha = np.arange(0, 2.5 * np.pi, 0.1)

    x = x0 + R * np.cos(alpha)
    y = y0 + R * np.sin(alpha)
    return x, y


# def astroida(R, t):
#     x = R * np.cos(t)**3
#     y = R * np.sin(t)**3
#     return x, y


X, Y = [], []
R = 1

def animate(i):
    X.append(cicloida(R=R, t=i)[0])
    Y.append(cicloida(R=R, t=i)[1])

    trajectory.set_data(X, Y)
    ball.set_data(cicloida(R=R, t=i))
    wells.set_data(weels_func(R, 0, R, 1, 0, t = i))
    

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('anim_cicloida.gif')

# def animate1(i):
#     graph.set_data(astroida(10, t=i))
