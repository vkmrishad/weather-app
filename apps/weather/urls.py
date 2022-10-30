from django.urls import path

# from apps.weather import views
from apps.weather.views import Home

app_name = 'weather'

urlpatterns = [
    path('', Home.as_view(), name="home"),
]