import matplotlib.pyplot as plt
import numpy as np


def log_spiral(b = 0.2):
    fi = np.arange(0, np.pi * 8, 0.0001)

    r = np.exp(b * fi)

    x = r * np.cos(fi)
    y = r * np.sin(fi)
    plt.plot(x, y)
    plt.grid()
    plt.savefig('pic1.png')


def arch_spiral(k = 2):
    fi = np.arange(0, np.pi * 8, 0.0001)

    r = k * fi

    x = r * np.cos(fi)
    y = r * np.sin(fi)
    plt.plot(x, y)
    plt.grid()
    plt.savefig('pic2.png')


def jezl_spiral(k = 2):
    fi = np.arange(0.01, np.pi * 8, 0.001)

    r = k / fi**0.5

    x = r * np.cos(fi)
    y = r * np.sin(fi)
    plt.plot(x, y)
    plt.grid()
    plt.savefig('pic3.png')


def rose(k = 8):
    fi = np.arange(0, np.pi * 8, 0.0001)

    r = np.sin(k * fi)

    x = r * np.cos(fi)
    y = r * np.sin(fi)
    plt.plot(x, y)
    plt.grid()
    plt.axis('equal')
    plt.savefig('pic4.png')


log_spiral()
arch_spiral()
jezl_spiral()
rose()
