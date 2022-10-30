import requests
from requests import RequestException

from django.conf import settings

# OPEN_WEATHER_MAP_API_KEY = settings.OPEN_WEATHER_MAP_API_KEY
API_KEY = "f0434074326407628f0a9af4fedb32d9"


def degree_to_direction_converter(degree):
    """
    Convert degree to cardinal direction
    :param degree:
    :return: cardinal direction
    """
    dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    calculate = int((degree + 11.25) / 22.5)
    return dirs[calculate % 16]


def fetch_weather_data(city):
    API_KEY = "f0434074326407628f0a9af4fedb32d9"

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=en&appid={API_KEY}"
        weather = requests.get(url.format(city)).json()
        print(weather)
    except ConnectionError as err:
        raise ConnectionError(err)
    except requests.exceptions.RequestException as err:
        raise RequestException(err)

    return weather


def weather_data(city):
    weather = fetch_weather_data(city)
    data = None

    # Map values if status is 200
    if weather and weather["cod"] == 200:
        data = {
            "city": weather["name"],
            "country": weather["sys"]["country"],
            "temperature": {
                "temp": round(weather["main"]["temp"]),
                "min": round(weather["main"]["temp_min"]),
                "max": round(weather["main"]["temp_max"])
            },
            "humidity": weather["main"]["humidity"],
            "pressure": weather["main"]["pressure"],
            "wind": {
                "speed": weather["wind"]["speed"],
                "direction": degree_to_direction_converter(weather["wind"]["deg"]),
            },
            "main": weather["weather"][0]["main"],
            "description": weather["weather"][0]["description"].capitalize(),
            "icon": weather["weather"][0]["icon"]
        }

    return data
