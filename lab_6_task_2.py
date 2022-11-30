import matplotlib.pyplot as plt
import numpy as np

def graph(nazv, *coeff):
    x = np.arange(-10, 10, 0.01)
    plt.axis('equal')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(nazv)
    plt.grid()
    
    if nazv == 'parabola':
        y = coeff[0] * x**2 + coeff[1] * x + coeff[2]
        plt.plot(x, y)
        plt.savefig('pic_1.png')
    elif nazv == 'giperbola':
        y = np.arange(-10, 10, 0.01)
        x, y = np.meshgrid(x, y)
        fxy = x**2 / coeff[0]**2 - y**2 / coeff[1] **2
        plt.contour(x, y, fxy, levels=[0])
        plt.savefig('pic_1.png')

graph('giperbola', 2, 3, 4)
