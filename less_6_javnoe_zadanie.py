import matplotlib.pyplot as plt
import numpy as np


def parabola_plotter(a=1, b=1, c=0, title='Parabola plotter'):
    x = np.arange(-11, 10, 0.001)
    y = a*x**2 + b*x + c

    plt.plot(x, y, label='Парабола')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend
    plt.axis('equal')
    plt.savefig('pic_1.png')


parabola_plotter()
