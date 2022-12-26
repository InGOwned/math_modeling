import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
circle1, = plt.plot([], [], '.', color='dimgray')
circle2, = plt.plot([], [], '.', color='dimgray')
circle3, = plt.plot([], [], '.', color='slategrey')
circle4, = plt.plot([], [], '.', color='slategrey')
circle5, = plt.plot([], [], '.', color='slategrey')
circle6, = plt.plot([], [], '.', color='azure')
circle7, = plt.plot([], [], '.', color='azure')
circle8, = plt.plot([], [], '.', color='azure')
circle9, = plt.plot([], [], '.', color='azure')
kassini, = plt.plot([], [], 'o', color='r')
# circle11, = plt.plot([], [], 'o', color='gray')

plt.plot([0], 'o', color='y', ms=50)

plt.axis('equal')
plt.grid()

edge = 3
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ax.set_facecolor("black")


def ring(r):
    fi = np.arange(0, np.pi * 2, 0.085)
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y



def sputnik(r, fi):
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y


def animate(i):
    circles_data = [(ring(r=0.7), circle1), (ring(r=0.77), circle2), (ring(r=1), circle3), (ring(r=1.07), circle4),
                    (ring(r=1.14), circle5), (ring(r=1.34), circle6), (ring(r=1.41), circle7), (ring(r=1.48), circle8),
                     (ring(r=1.55), circle9)]

    for (x, y), circle in circles_data:
        X_rotate = x * np.cos(i) - y * np.sin(i)
        Y_rotate = y * np.cos(i) + x * np.sin(i)
        circle.set_data(X_rotate, Y_rotate)
    for n in range(20000):
        kassini.set_data(sputnik(r=1.41, fi=n))


ani = FuncAnimation(fig,
                    animate,
                    frames=np.arange(0, np.pi * 8, 0.08),
                    interval=30)
ani.save('Saturn_test.gif')
