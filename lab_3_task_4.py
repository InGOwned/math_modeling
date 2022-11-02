import numpy as np
M = 5
N = 10

A = np.zeros((N, M))

for i in range(1, M):
  for j in range(1, M):
    A[i, j] = np.sin(N * i + M * j)
    if A[i, j] < 0:
      A[i, j] = 0

print(A)
