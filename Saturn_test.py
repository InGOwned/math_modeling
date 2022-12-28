import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
circle1, = plt.plot([], [], '.', color='darkgray')
circle2, = plt.plot([], [], '.', color='darkgray')
circle3, = plt.plot([], [], '.', color='dimgray')
circle4, = plt.plot([], [], '.', color='slategrey')
circle5, = plt.plot([], [], '.', color='slategrey')
circle6, = plt.plot([], [], '.', color='azure')
circle7, = plt.plot([], [], '.', color='azure')
circle8, = plt.plot([], [], '.', color='azure')
circle9, = plt.plot([], [], '.', color='azure')
circle10, = plt.plot([], [], '.', color='azure')
circle11, = plt.plot([], [], '.', color='lightsteelblue')
circle12, = plt.plot([], [], '.', color='lightsteelblue')
Pan, = plt.plot([], [], 'o', color='lightcoral', ms=7.5)
Daphnis, = plt.plot([], [], 'o', color='maroon', ms=7)
Atlas, = plt.plot([], [], 'o', color='chocolate', ms=7)
Pandora, = plt.plot([], [], 'o', color='mistyrose', ms=8)


plt.plot([0], 'o', color='y', ms=60)

plt.axis('equal')

edge = 2.75
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ax.set_facecolor("black")

plt.title('Saturn and its rings')
ax.text(0, 0, 'Saturn', ha='center', va='center', color='w', fontsize=15)

ax.legend([Pan, Daphnis, Pandora, Atlas], ['Pan', 'Daphnis', 'Pandora', 'Atlas'])


def ring(r):
    fi = np.arange(0, np.pi * 2, 0.085)
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y


def sputnik(r, fi, angle):
    x = r * np.cos(fi + angle)
    y = r * np.sin(fi + angle)
    return x, y


speeds = {circle1: 8, circle2: 7, circle3: 6, circle4: 5, circle5: 5, circle6: 4, circle7: 3,
          circle8: 3, circle9: 3, circle10: 3, circle11: 2, circle12: 1}


def animate(i):
    circles_list = [(ring(r=0.7), circle1), (ring(r=0.77), circle2), (ring(r=0.87), circle3), (ring(r=0.97), circle4),
                    (ring(r=1.04), circle5), (ring(r=1.14), circle6), (ring(r=1.24), circle7), (ring(r=1.32), circle8),
                    (ring(r=1.40), circle9), (ring(r=1.48), circle10), (ring(r=1.68), circle11),
                    (ring(r=1.76), circle12),
                    (sputnik(r=1.68, fi=i1, angle=-1), Pan),
                    (sputnik(r=1.76, fi=i1, angle=2.3), Daphnis),
                    (sputnik(r=1.76, fi=i1, angle=1.2), Atlas),
                    (sputnik(r=2.1, fi=i1, angle=3), Pandora)]

    for (x, y), circle in circles_list:
        if circle == Pan:
            X_rotate = x * np.cos(-i * speeds.get(circle11)) - y * np.sin(-i * speeds.get(circle11))
            Y_rotate = y * np.cos(-i * speeds.get(circle11)) + x * np.sin(-i * speeds.get(circle11))
            circle.set_data(X_rotate, Y_rotate)
        elif circle == Daphnis or circle == Atlas:
            X_rotate = x * np.cos(-i * speeds.get(circle12)) - y * np.sin(-i * speeds.get(circle12))
            Y_rotate = y * np.cos(-i * speeds.get(circle12)) + x * np.sin(-i * speeds.get(circle12))
            circle.set_data(X_rotate, Y_rotate)
        elif circle == Pandora:
            X_rotate = x * np.cos(-i) - y * np.sin(-i)
            Y_rotate = y * np.cos(-i) + x * np.sin(-i)
            circle.set_data(X_rotate, Y_rotate)
        else:
            X_rotate = x * np.cos(-i * speeds.get(circle)) - y * np.sin(-i * speeds.get(circle))
            Y_rotate = y * np.cos(-i * speeds.get(circle)) + x * np.sin(-i * speeds.get(circle))
            circle.set_data(X_rotate, Y_rotate)


ani = FuncAnimation(fig,
                    animate,
                    frames=np.arange(0, np.pi * 8, 0.08),
                    interval=60)
ani.save('Saturn_test.gif')
