import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='g')

x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)

def butterfly():
   t = np.arange(0, 12 * np.pi, 0.01)
   x = sin(t) * (np.exp(cos(t) - 2 * cos(4 * t) + sin(t / 12)**5))
   y = cos(t) * (np.exp(cos(t) - 2 * cos(4 * t) + sin(t / 12)**5))
 
edge = 100000
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
def animate():
    ball.set_data(butterfly())
    
ani = animation.FuncAnimation(fig, animate, frames=130, interval=30)
 
ani.save('butterfly.gif')