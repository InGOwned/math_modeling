import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
 
fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='b', label='Ball')
 
def circle_move(R, k, time):
    R = k * time
    fi = np.arange(0, 2*np.pi, 0.1)
    x = R * np.cos(fi)
    y = R * np.sin(fi)
    return x, y
 
edge = 100
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
def animate(i):
    ball.set_data(circle_move(R=1, k=1, time=i))
    
ani = animation.FuncAnimation(fig, animate, frames=130, interval=30)
 
ani.save('lab_7_circle.gif')
