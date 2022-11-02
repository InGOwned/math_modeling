import numpy as np
from lab_3_task_4 import A, N, M

A1 = np.zeros((N, M))
for i in range(N):
  for j in range(M):
    A1[i, j] = A[i, j]
print()

slice1 = A[:, 0]
slice2 = A[:, 1]

slice1, slice2 = slice2, slice1

print(A1)