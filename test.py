import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np



fi = np.arange(0, np.pi * 8, 0.1)

def ellipse(p = 3, e = 0.65):
    
    r = p / (1 + (ee * np.cos(ee)))

    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y