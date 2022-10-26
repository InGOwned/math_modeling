import numpy as np

a = np.zeros((3, 3))
print(a)

a[0, 2] = 5
print(a)

b = np.ones((3, 3))
print(b)
print(type(b))

d = np.ndarray((3, 2))
print(d)