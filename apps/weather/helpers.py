import asyncio
import aiohttp
import requests
from requests import RequestException

from django.utils.translation import get_language
from django.conf import settings

OPEN_WEATHER_MAP_API_KEY = settings.OPEN_WEATHER_MAP_API_KEY


def degree_to_direction_converter(degree):
    """
    Convert degree to cardinal direction
    :param degree:
    :return: cardinal direction
    """
    dirs = [
        "N",
        "NNE",
        "NE",
        "ENE",
        "E",
        "ESE",
        "SE",
        "SSE",
        "S",
        "SSW",
        "SW",
        "WSW",
        "W",
        "WNW",
        "NW",
        "NNW",
    ]
    calculate = int((degree + 11.25) / 22.5)
    return dirs[calculate % 16]


async def fetch_weather_data(city, lang):
    """
    Fetch waether data from OpenWeatherMap API
    :param city:
    :return:
    """
    API = "https://api.openweathermap.org/data/2.5/weather"

    try:
        url = f"{API}?q={city}&units=metric&lang={lang}&appid={OPEN_WEATHER_MAP_API_KEY}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
    except ConnectionError as err:
        raise ConnectionError(err)
    except requests.exceptions.RequestException as err:
        raise RequestException(err)


def weather_data(city):
    """
    Mapping OpenWeatherMap API to defined structure
    :param city:
    :return:
    """
    # Current selected language
    lang = get_language()

    weather = asyncio.run(fetch_weather_data(city, lang))
    data = None

    # Map values if status is 200
    if weather and weather["cod"] == 200:
        data = {
            "city": weather["name"],
            "country": weather["sys"]["country"],
            "temperature": {
                "temp": round(weather["main"]["temp"]),
                "min": round(weather["main"]["temp_min"]),
                "max": round(weather["main"]["temp_max"]),
            },
            "humidity": weather["main"]["humidity"],
            "pressure": weather["main"]["pressure"],
            "wind": {
                "speed": weather["wind"]["speed"],
                "direction": degree_to_direction_converter(
                    weather["wind"]["deg"]
                ),
            },
            "main": weather["weather"][0]["main"],
            "description": weather["weather"][0]["description"].capitalize(),
            "icon": weather["weather"][0]["icon"],
        }

    return data
