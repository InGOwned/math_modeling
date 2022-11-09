from constants import g
def full_energy(m, h, v):
  E = m * g * h + v**2/2
  return E
print(full_energy(10, 15, 20))