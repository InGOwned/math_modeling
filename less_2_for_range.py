for i in range(1, 5):
  print(i , i**2, sep=' ; ')

print()

a = [1, 2, 3, 4, 5]
for i in a:
  print(f'{i}**3 = {i**3}')

print()

a = range(0, 10, 2)
print(a)
print(type(a))
print(a[3])

print()

a = 'good'
for i in range(10):
  if i < len(a):
    print(a[i] + ' - bad')
  else:
    print(f'{i} - good')