import matplotlib as plt
import numpy as np

def circle_plotter(raduis=10):
    x = np.arange(-2 * raduis, 2 * raduis, 0.1)
    y = np.arange(-2 * raduis, 2 * raduis, 0.1)

    X, Y = np.meshgrid(x, y)
    fxy = X**2 + Y**2 - raduis**2

    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal')
    plt.savefig('pic_1.png')

