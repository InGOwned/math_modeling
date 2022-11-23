import matplotlib.pyplot as plt
import numpy as np

def graph(a, b, c, nazv, xa, xb, N):
    x = np.linspace(xa, xb, N)
    y1 = 1 / x
    y2 = a * x**2 + b * x + c
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.savefig('pic_1.png')

graph(2, 3, 4, 'Гипербола', -10, 10, 0.01)
