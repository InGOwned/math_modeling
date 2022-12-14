from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
figure, = plt.plot([], [], '-', color='b')

plt.axis('equal')


def butterfly(t):
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12)**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12)**5)
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.5, 5.5)
    return x, y


def heart(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(3 * t)
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    return x, y


x1 = []
y1 = []


def animate(t):
    x1.append(butterfly(t)[0])
    y1.append(butterfly(t)[1])
    figure.set_data(x1, y1)
    return figure,

x2 = []
y2 = []

def animate1(t):
    x2.append(heart(t)[0])
    y2.append(heart(t)[1])
    figure.set_data(x2, y2)
    return figure,


ani = FuncAnimation(fig, animate, frames=np.arange(0, 2 * np.pi, 0.01), interval=30)
ani.save('butterfly.gif')

ani = FuncAnimation(fig, animate1, frames=np.arange(0, 2 * np.pi, 0.01), interval=30)
ani.save('heart.gif')
