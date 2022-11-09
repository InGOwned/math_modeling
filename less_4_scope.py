x1 = 10

def move(t):
  x = x1 * t
  return x

print(move(3))
# print(x)

a = 'good'

def my_func():
  a = 'bad'
  print(a)

my_func()
print(a)
