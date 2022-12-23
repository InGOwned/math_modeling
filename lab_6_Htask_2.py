import matplotlib.pyplot as plt
import numpy as np


def ellips(e = 0.65, p = 3):
    fi = np.arange(0, np.pi * 8, 0.001)

    r = p / (1 + e * np.cos(fi))

    x = r * np.cos(fi)
    y = r * np.sin(fi)
    plt.plot(x, y)
    plt.grid()
    plt.axis('equal')
    plt.savefig('pic_1.png')


ellips()
