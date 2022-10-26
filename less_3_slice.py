import numpy as np

a = [i for i in range(10)]

s = a[0:5:2]
print(s)

s = a[::-1]
print(s)

b = np.array([a, np.array(a) * 3])
print(b)
s = b[::, 1]
print(s)

s = b[1,2::1]
print(s)
