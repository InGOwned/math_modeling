import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
 
fig, ax = plt.subplots()
frakt, = plt.plot([], [], '-', color='r')

plt.axis('equal')

def mn(x0, y0, C, D):
     n = np.arange(x0, y0, 0.01)
     x = x0**2 - y0**2 + C
     y = 2 * x0 * y0 + D
     