import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import shelve
import time

# Ваш API ключ
api_key = "4b48e8d03f1aede58b50beff49f35b92"

# Список городов
cities = ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Kazan"]

# URL для запроса погоды
base_url = "http://api.openweathermap.org/data/2.5/weather"

# Словарь для хранения координат и температур
data = {}

# Время жизни кэша (например, 3600 секунд = 1 час)
cache_lifetime = 3600

# Открываем кэш-файл
with shelve.open('weather_cache') as cache:
    current_time = time.time()
    for city in cities:
        # Проверяем наличие данных в кэше и их актуальность
        if city in cache and current_time - cache[city]['timestamp'] < cache_lifetime:
            print(f"Используем кэшированные данные для {city}")
            data[city] = cache[city]['data']
        else:
            # Выполняем запрос к API
            params = {
                'q': city,
                'appid': api_key,
                'units': 'metric'
            }
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                weather_data = response.json()
                lat = weather_data['coord']['lat']
                lon = weather_data['coord']['lon']
                temp = weather_data['main']['temp']
                data[city] = {'lat': lat, 'lon': lon, 'temp': temp}
                # Сохраняем данные в кэш
                cache[city] = {
                    'data': data[city],
                    'timestamp': current_time
                }
            else:
                print(f"Не удалось получить данные для {city}")
                print(f"Status Code: {response.status_code}")
                print(f"Response: {response.text}")

# Создаем карту
fig, ax = plt.subplots(figsize=(10, 8))
m = Basemap(projection='merc', llcrnrlat=40, urcrnrlat=70, llcrnrlon=20, urcrnrlon=180, resolution='i')

m.drawcoastlines()
m.drawcountries()
m.drawmapboundary()

# Добавляем города и температуру на карту
for city, info in data.items():
    x, y = m(info['lon'], info['lat'])
    plt.text(x, y, f"{city}\n{info['temp']}°C", fontsize=12, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.6, edgecolor='black'))

# Показываем карту
plt.title('Current Temperature in Russian Cities')
plt.show()