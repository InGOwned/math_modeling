def changer(a:int, b:list):
  a = 2
  b[0] = 'good'

x = 10
L = [1, 2]

changer(x, L)
print(x)
print(L)

# complex numbers

x = 4
y = 5

z = complex(x, y)
print(z)

w = complex(y, x)
print(z + w)

# Tuple

t = (1, 4, 8)
print(t[0])
print()
# t[0] = 2

# Dict

d = {'a1':4, 'a2':'Hello'}
print(d["a1"])
print(d["a2"])

d["a2"] = 'Bad'
print(d)
