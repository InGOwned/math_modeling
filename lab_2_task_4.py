a = int(input())
a1 = a2 = 1
print(1, 1, end=' ')

for i in range(1, a):
  b = a1 + a2
  print(b, end=' ')
  a1, a2 = a2, b 
