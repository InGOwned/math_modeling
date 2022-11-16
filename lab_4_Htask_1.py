def func(a, n):
  a0 = a
  for i in range(1, n):
    a *= a0
  print(a)


a = abs(int(input()))
n = int(input())
func(a, n)
