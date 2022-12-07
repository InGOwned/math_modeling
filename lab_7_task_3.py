from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='g')

def butterfly():
   t = np.arange(0, 12 * np.pi, 0.01)
   x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12)**5)
   y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12)**5)
   return x, y

plt.axis('equal')
ax.set_xlim(-5.5, 5.5)
ax.set_ylim(-5.5, 5.5)

def animate(i):
    ball.set_data(butterfly())
    return ball,

ani = FuncAnimation(fig, animate, interval=30)

ani.save('butterfly.gif')
