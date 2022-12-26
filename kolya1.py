import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np 
 
fig, ax = plt.subplots() 
ball, = plt.plot([], [], 'o', color='b') 
ball1, = plt.plot([], [], 'o', color='b') 
trajectory, = plt.plot([], [], '-', color='g') 
trajectory1, = plt.plot([], [], '-', color='g') 
 
frames = np.arange(0, 4.85 * np.pi, 0.06) 
plt.axis('equal') 
ax.set_xlim(-10, 10) 
ax.set_ylim(-10, 10) 
 
def circle_move1(R, alpha): 
    x = R * np.cos(2*np.pi*alpha/2.36*10**6) 
    y = R * np.sin(2*np.pi*alpha/2.36*10**6) 
    return x, y 
 
def circle_move(R, alpha): 
    x = R * np.cos(2*np.pi*alpha/T1) 
    y = R * np.sin(2*np.pi*alpha/T1) 
    return x, y 
 
X, Y = [], [] 
x1, y1 = [], [] 
R = 3 
N=1000.0 
T1=3.156*10**7 
alpha = [T1 * i / N for i in np.arange(0,N,1)] 
XG = X + x1 
YG = Y + y1 
 
def animate(i): 
    X.append(circle_move(R=R, alpha=i)[0]) 
    XG.append(circle_move1(R=R, alpha=i)[0]) 
    Y.append(circle_move(R=R, alpha= i)[1]) 
    YG.append(circle_move1(R=R, alpha= i)[1]) 
    ball.set_data(circle_move(R=R, alpha=i)) 
    ball1.set_data(circle_move1(R=R, alpha=i)) 
    trajectory.set_data(X, Y) 
    trajectory1.set_data(XG, YG) 
    return ball, 
 
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=100) 
ani.save('test1.gif')