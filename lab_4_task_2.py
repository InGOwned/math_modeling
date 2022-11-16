def mult(a):
  elem = 1
  for x in a:
    elem *= x
  return elem

print(mult([1, 2, 3, 4, 8, 9, 11]))