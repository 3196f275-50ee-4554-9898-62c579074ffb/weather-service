import requests
from flask import Flask, jsonify, render_template_string
import folium
import pickle
import os
import time

app = Flask(__name__)

# API KEY OpenWeather
api_key = "4b48e8d03f1aede58b50beff49f35b92"
api_key_geo = "4b48e8d03f1aede58b50beff49f35b92"

krasnodar_coords = (45.0355, 38.9753)

# Радиус поиска городов (в километрах)
radius = 100

# API для запроса погоды и городов
base_url = "http://api.openweathermap.org/data/2.5/weather"
geo_url = "http://api.openweathermap.org/data/2.5/find"

# Время жизни кэша (например, 3600 секунд = 1 час)
cache_lifetime = 3600
cache_filename = 'weather_cache.pkl'

# Функция для загрузки кэша
def load_cache():
    if os.path.exists(cache_filename):
        with open(cache_filename, 'rb') as f:
            return pickle.load(f)
    return {}

# Функция для сохранения кэша
def save_cache(cache):
    with open(cache_filename, 'wb') as f:
        pickle.dump(cache, f)

# Функция для получения данных о погоде
def get_weather_data():
    # Загружаем кэш
    cache = load_cache()
    current_time = time.time()

    # Получаем список городов в радиусе от Краснодара
    params_geo = {
        'lat': krasnodar_coords[0],
        'lon': krasnodar_coords[1],
        'cnt': 50,  # Максимальное количество городов
        'radius': radius * 1000,  # Радиус в метрах
        'appid': api_key_geo
    }

    response_geo = requests.get(geo_url, params=params_geo)
    if response_geo.status_code == 200:
        city_data = response_geo.json()['list']
    else:
        return {"error": "Не удалось получить список городов"}

    data = {}
    for city in city_data:
        city_name = city['name']
        if city_name in cache and current_time - cache[city_name]['timestamp'] < cache_lifetime:
            print(f"Используем кэшированные данные для {city_name}")
            data[city_name] = cache[city_name]['data']
        else:
            params_weather = {
                'q': city_name,
                'appid': api_key,
                'units': 'metric'
            }
            response_weather = requests.get(base_url, params=params_weather)
            if response_weather.status_code == 200:
                weather_data = response_weather.json()
                lat = weather_data['coord']['lat']
                lon = weather_data['coord']['lon']
                temp = weather_data['main']['temp']
                data[city_name] = {'lat': lat, 'lon': lon, 'temp': temp}
                # Сохраняем данные в кэш
                cache[city_name] = {
                    'data': data[city_name],
                    'timestamp': current_time
                }
            else:
                print(f"Не удалось получить данные для {city_name}")
                print(f"Status Code: {response_weather.status_code}")
                print(f"Response: {response_weather.text}")

    # Сохраняем кэш
    save_cache(cache)

    return data

@app.route('/weather', methods=['GET'])
def get_weather():
    data = get_weather_data()
    return jsonify(data)

@app.route('/map', methods=['GET'])
def get_map():
    data = get_weather_data()

    # Создаем карту с использованием folium
    m = folium.Map(location=krasnodar_coords, zoom_start=10)

    # Добавляем города и температуру на карту
    for city, info in data.items():
        folium.Marker(
            location=[info['lat'], info['lon']],
            popup=f"{city}: {info['temp']}°C",
            tooltip=city
        ).add_to(m)

    # Сохраняем карту в строку HTML
    map_html = m._repr_html_()

    # Используем шаблон для отображения карты
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Карта Погоды</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <h1>Карта Погоды</h1>
        {{ map_html|safe }}
    </body>
    </html>
    """

    # Возвращаем страницу с картой
    return render_template_string(template, map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)