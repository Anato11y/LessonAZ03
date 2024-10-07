import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL страницы с диванами
url = 'https://www.divan.ru/irkutsk/category/divany-i-kresla'

# Отправка запроса на сайт
response = requests.get(url)
response.raise_for_status()  # Проверка на успешное выполнение запроса

# Создание объекта BeautifulSoup для парсинга
soup = BeautifulSoup(response.text, 'html.parser')

# Инициализация списков для хранения данных
names = []
prices = []
urls = []

# Найдите элементы, соответствующие диванам и их ценам (проверьте структуру сайта)
for item in soup.select('div._Ud0k'):  # Обновите селектор в зависимости от структуры сайта
    name = item.select_one('div.lsooF span').get_text(strip=True) if item.select_one('div.lsooF span') else 'Не указано'
    price_text = item.select_one('div.pY3d2 span').get_text(strip=True) if item.select_one('div.pY3d2 span') else '0'
    url_suffix = item.select_one('a')['href'] if item.select_one('a') else ''

    # Удаляем любые нечисловые символы из цены и преобразуем в число
    price = int(''.join(filter(str.isdigit, price_text)))

    names.append(name)
    prices.append(price)
    urls.append(f"https://www.divan.ru{url_suffix}")

# Создание DataFrame
df = pd.DataFrame({
    'Название': names,
    'Цена': prices,
    'Ссылка': urls
})

# Сохранение данных в CSV
df.to_csv('divan_prices.csv', index=False)

# Вычисление средней цены
average_price = df['Цена'].mean()
print(f"Средняя цена на диваны: {average_price} руб.")

# Построение гистограммы цен
plt.figure(figsize=(10, 6))
plt.hist(df['Цена'], bins=20, color='skyblue', edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (рубли)')
plt.ylabel('Количество')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

