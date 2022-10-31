from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse

from apps.weather.helpers import degree_to_direction_converter, weather_data

berlin_weather_data = {
    "coord": {"lon": 13.4105, "lat": 52.5244},
    "weather": [
        {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01n",
        }
    ],
    "base": "stations",
    "main": {
        "temp": 12.65,
        "feels_like": 12.22,
        "temp_min": 9.01,
        "temp_max": 15.65,
        "pressure": 1009,
        "humidity": 86,
    },
    "visibility": 10000,
    "wind": {"speed": 2.06, "deg": 250},
    "clouds": {"all": 0},
    "dt": 1667193523,
    "sys": {
        "type": 2,
        "id": 2011538,
        "country": "DE",
        "sunrise": 1667196019,
        "sunset": 1667230769,
    },
    "timezone": 3600,
    "id": 2950159,
    "name": "Berlin",
    "cod": 200,
}


class TestPage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_degree_to_direction_converter_fn(self):
        dir = degree_to_direction_converter(340)
        self.assertEqual(dir, "NNW")

    def test_weather_data_fn(self):
        expected_data = {
            "city": "Berlin",
            "country": "DE",
            "temperature": {"temp": 13, "min": 9, "max": 16},
            "humidity": 86,
            "pressure": 1009,
            "wind": {"speed": 2.06, "direction": "WSW"},
            "main": "Clear",
            "description": "Clear sky",
            "icon": "01n",
        }

        with patch(
            "apps.weather.helpers.fetch_weather_data",
            return_value=berlin_weather_data,
        ):
            data = weather_data("Berlin")
            self.assertEqual(data, expected_data)

    def test_index_page_english(self):
        # Switch language
        self.client = Client(HTTP_ACCEPT_LANGUAGE="en")

        # Override fetch_weather_data from OpenWeatherMap API
        with patch(
            "apps.weather.helpers.fetch_weather_data",
            return_value=berlin_weather_data,
        ):
            url = reverse("weather:home")
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "index.html")
            self.assertContains(response, "Berlin")
            self.assertContains(response, "Clear")
            self.assertContains(response, "Clear sky")
            self.assertContains(response, "Weather")
            self.assertContains(response, "City")
            self.assertContains(response, "Temperature")
            self.assertContains(response, "Low")
            self.assertContains(response, "High")
            self.assertContains(response, "Wind")
            self.assertContains(response, "Humidity")
            self.assertContains(response, "Pressure")

    def test_index_page_german(self):
        # Switch language
        self.client = Client(HTTP_ACCEPT_LANGUAGE="de")

        # Override fetch_weather_data from OpenWeatherMap API
        with patch(
            "apps.weather.helpers.fetch_weather_data",
            return_value=berlin_weather_data,
        ):
            url = reverse("weather:home")
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "index.html")
            self.assertContains(response, "Berlin")
            self.assertContains(response, "Clear")
            self.assertContains(response, "Clear sky")
            self.assertContains(response, "Wetter")
            self.assertContains(response, "Stadt")
            self.assertContains(response, "Temperatur")
            self.assertContains(response, "Niedrig")
            self.assertContains(response, "Hoch")
            self.assertContains(response, "Wind")
            self.assertContains(response, "Feuchtigkeit")
            self.assertContains(response, "Druck")

    def test_index_page_spanish(self):
        # Switch language
        self.client = Client(HTTP_ACCEPT_LANGUAGE="es")

        # Override fetch_weather_data from OpenWeatherMap API
        with patch(
            "apps.weather.helpers.fetch_weather_data",
            return_value=berlin_weather_data,
        ):
            url = reverse("weather:home")
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "index.html")
            self.assertContains(response, "Berlin")
            self.assertContains(response, "Clear")
            self.assertContains(response, "Clear sky")
            self.assertContains(response, "Clima")
            self.assertContains(response, "La ciudad")
            self.assertContains(response, "La temperatura")
            self.assertContains(response, "Bajo")
            self.assertContains(response, "Alto")
            self.assertContains(response, "Viento")
            self.assertContains(response, "Humedad")
            self.assertContains(response, "Presión")

    def test_index_page_french(self):
        # Switch language
        self.client = Client(HTTP_ACCEPT_LANGUAGE="fr")

        # Override fetch_weather_data from OpenWeatherMap API
        with patch(
            "apps.weather.helpers.fetch_weather_data",
            return_value=berlin_weather_data,
        ):
            url = reverse("weather:home")
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "index.html")
            self.assertContains(response, "Berlin")
            self.assertContains(response, "Clear")
            self.assertContains(response, "Clear sky")
            self.assertContains(response, "Météo")
            self.assertContains(response, "Ville")
            self.assertContains(response, "Température")
            self.assertContains(response, "Faible")
            self.assertContains(response, "Élevé")
            self.assertContains(response, "Vent")
            self.assertContains(response, "Humidité")
            self.assertContains(response, "Pression")
