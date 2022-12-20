import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
star, = plt.plot([], [], '-', color='r')
plt.axis('equal')

t = np.arange(0, 4 * np.pi, 0.01)


# функция, возвращающая координаты точек звезды
def star_points():
  x = 12 * np.cos(t) + 8 * np.cos(1.5*t)
  y = 12 * np.sin(t) - 8 * np.sin(1.5*t)
  return x, y


# функция анимации
def animate(i):
  x, y = star_points()
  X = x * np.cos(i) - y * np.sin(i)
  Y = y * np.cos(i) + x * np.sin(i)
  star.set_data(X, Y)
  return star,


ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)


# создаем анимацию
ani = animation.FuncAnimation(fig, animate, frames=300, interval=300)

ani.save('star.gif')
