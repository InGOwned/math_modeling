a, b = int(input()), int(input())

if a % b == 0:
  print("Делится")
  print(a // b)
else:
  print(f"{a} на {b} не делится")
  print("Остаток от деления равен", a % b)
  print("результат деления равен", a / b)
