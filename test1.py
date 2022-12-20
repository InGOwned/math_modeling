import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def update(i, circle):
    angle = np.deg2rad(i) # угол качения в радианах
    x = np.cos(angle) # координата x круга
    y = np.sin(angle) # координата y круга
    circle.set_data(x, y)
    return circle,


fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
circle, = ax.plot([], [], 'bo', markersize=10)
anim = FuncAnimation(fig, update, frames=360, fargs=(circle,), interval=20)

anim.save('test1.gif')

