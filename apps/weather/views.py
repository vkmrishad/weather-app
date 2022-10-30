import re
import requests

from django.views.generic import TemplateView

from apps.weather.helpers import degree_to_direction_converter, weather_data


class Home(TemplateView):
    """
    View for App Store AppHome
    """
    template_name = 'index.html'
    context_object_name = 'data'

    def get(self, request, *args, **kwargs):
        query_params = self.request.GET

        city = query_params.get("city")

        data = None
        if city:
            city = re.sub('\s+', ' ', city).strip()

            # Fetch weather data from openweathermap API
            data = weather_data(city)

        context = self.get_context_data(**kwargs)
        context["data"] = data
        return self.render_to_response(context)
