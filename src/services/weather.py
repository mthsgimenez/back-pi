import requests

def getCurrentWeather():
    uri = 'https://api.open-meteo.com/v1/forecast?latitude=-25.4278&longitude=-49.2731&daily=temperature_2m_max,temperature_2m_min,wind_speed_10m_max,weather_code,rain_sum&timezone=America%2FSao_Paulo&forecast_days=1'
    try:
        response = requests.get(uri)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        return { 'error': f'HTTP error: {err}' }
    except Exception as err:
        return { 'error': err }