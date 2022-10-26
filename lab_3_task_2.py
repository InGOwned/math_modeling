import numpy as np
import constants as cons

h = 100
b = 30
a = np.pi / 3
T = 200
e = 300

v = ((cons.g * h * np.tan(b)**2)/(2 * np.cos(a)**2 * (1 - np.tan(b) * np.tan(a))))**0.5
print(v)

N = (2 / np.pi**0.5) * (cons.h / (cons.k * T)**1.5) * np.exp(-e / (cons.k * T)) * e**(T/2)
print(N)
