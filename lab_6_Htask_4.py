import matplotlib.pyplot as plt


def draw_ladder(num_steps):
  x = []
  y = []
  for n in range(num_steps):
      x += [n, n+1]
      y += [n, n]
  plt.plot(x, y, color='k')
  plt.savefig('ladder.png')


draw_ladder(5)
