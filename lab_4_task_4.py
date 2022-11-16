import numpy as np
np.

def func(a, b, N):
  x = np.linspace(a, b, N)
  y = x ** 2
  print(y)


func(int(input()), int(input()), int(input()))