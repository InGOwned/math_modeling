import matplotlib.pyplot as plt
import numpy as np


def func(x, a, b):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] < a:
            y[i] = a**2
        elif a <= x[i] <= b:
            y[i] = x[i]**2
        else:
            y[i] = b**2
    
    return y
    

x = np.linspace(-100, 100, 1000)

y = func(x, -23, -24)

plt.plot(x, y)
plt.savefig("pic_1.png")
