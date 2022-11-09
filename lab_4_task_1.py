def srednee(a):
  s = 0
  for x in a:
    s += x
  return s / len(a)

print(srednee([2, 3, 10, 12, 20]))
