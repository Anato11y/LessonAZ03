import numpy as np
import matplotlib.pyplot as plt

# Параметры для нормального распределения
mean = 0  # Среднее значение
std_dev = 1  # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация данных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы для нормального распределения
plt.figure(figsize=(10, 5))
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Генерация данных для диаграммы рассеяния
data_x = np.random.rand(100)  # Первый набор случайных данных
data_y = np.random.rand(100)  # Второй набор случайных данных

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 5))
plt.scatter(data_x, data_y, alpha=0.7, color='purple', edgecolor='black')
plt.title('Диаграмма рассеяния двух случайных наборов данных')
plt.xlabel('Набор данных X')
plt.ylabel('Набор данных Y')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
