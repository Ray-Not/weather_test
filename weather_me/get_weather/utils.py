import requests
from datetime import datetime


def get_coordinates(city):
    url = f'https://nominatim.openstreetmap.org/search?q={city}&format=json'
    headers = {
        'User-Agent': 'GetWeather/1.0 (2sinsincuba@gmail.com)'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            latitude = float(data[0]['lat'])
            longitude = float(data[0]['lon'])
            return latitude, longitude
        return None, f"Город {city} не найден."
    return None, f"Ошибка при выполнении запроса: {response}"


def get_weather(city):
    lat, lng_or_error = get_coordinates(city)
    if lat is None:
        return {'error': lng_or_error}
    current_date = datetime.now().date()
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'hourly': 'temperature_2m',
        'latitude': lat,
        'longitude': lng_or_error,
        'timezone': 'auto',
        'start_date': current_date.strftime('%Y-%m-%d'),
        'end_date': current_date.strftime('%Y-%m-%d'),
        }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        times = data.get('hourly', {}).get('time', [])
        temperatures = data.get('hourly', {}).get('temperature_2m', [])
        if not times or not temperatures:
            return {'error': 'Данные не соответствуют ожиданиям'}
        split_times = [time.split('T') for time in times]
        times = [item[1] for item in split_times]
        return {'times': times, 'temperatures': temperatures}
    except requests.RequestException as e:
        return {'error': str(e)}
