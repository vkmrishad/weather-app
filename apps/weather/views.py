import re

from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from django.views.generic import TemplateView

from apps.weather.helpers import weather_data


class Home(TemplateView):
    """
    View for App Store AppHome
    """

    template_name = "index.html"
    context_object_name = "data"

    @method_decorator(cache_page(settings.CUSTOM_CACHE_SECONDS))
    def get(self, request, *args, **kwargs):
        query_params = self.request.GET

        city = query_params.get("city", "Berlin")

        data = None
        if city:
            city = re.sub("\s+", " ", city).strip()

            # Fetch weather data from openweathermap API
            data = weather_data(city)

        context = self.get_context_data(**kwargs)
        context["data"] = data
        return self.render_to_response(context)
