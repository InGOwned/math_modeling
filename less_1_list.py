a = [1, 2, 3]
print(a[1])

b = [4, 5, 6]

c = a + b
print(*c)

#c = a - b

print(*(c * 2))

print(len(a))

a.append(b)
print(a[3][1])