def mult(a):
  elem = 1
  s = 0
  for x in a:
    s += elem * x
    elem = x
  return s

print(mult([1, 2, 3, 4, 8, 9, 11]))