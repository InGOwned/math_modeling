import matplotlib.pyplot as plt
import numpy as np


def figura(A = 1, B = 10, a = 1, b = 2):
    t = np.arange(-10, 10, 0.0001)
    
    x = (A * (np.sin(a * t + np.pi / 2)))
    y = (B * (np.sin(b * t)))

    plt.plot(x, y)
    plt.grid()
    plt.savefig('pic_1.png')

figura()
