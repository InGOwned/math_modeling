import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# генерируем набор данных соответствующий нормальному распределению
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=50, density=True)
plt.show()

# генерируем значения x для построения графика теоретического распределения
x = np.linspace(-5, 5, 1000)

# расчитываем значения y для построения графика теоретического распределения
y = norm.pdf(x, 0, 1)

# рисуем график теоретического распределения на той же оси y, что и гистограмма
plt.plot(x, y, 'r-')
plt.savefig('test.png')
