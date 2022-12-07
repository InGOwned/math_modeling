import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() # Создание пространства и подпространства

anim_object, = plt.plot([], [], '-', lw=2) # Объект анимации

xdata, ydata = [], [] # Координаты объекта анимации

ax.set_xlim(0, 2*np.pi) # Пределы изменения переменной X
ax.set_ylim(-1, 1) # Пределы изменения переменной Y

def animate(frame): # Функция подстановки координат в объект анимации
    xdata.append(frame) # Расчёт координаты X
    ydata.append(np.cos(frame)) # Расчёт координаты Y
    anim_object.set_data(xdata, ydata) # Передача координата 
    return anim_object,

ani = FuncAnimation(fig, animate, frames=np.arange(0, 2*np.pi, 0.01), interval=30)
ani.save("less_7_create_animation.gif")
