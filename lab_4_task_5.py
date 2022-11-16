import numpy as np


def func(*args, **kw):
  if kw['figure'] == 'rectangle':
    s = args[0]*args[1]
  elif kw['figure'] == 'circle':
    s = np.pi * args[0]**2
  elif kw['figure'] == 'triangle':
    s = args[0] * args[1] / 2
  print(s)


func(10, 16, figure = input())
