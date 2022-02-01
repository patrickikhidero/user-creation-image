import pytest
from django.urls import resolve, reverse



pytestmark = pytest.mark.django_db


def test_register():
    assert reverse("users:register") == "/register-users"
    assert resolve("/api/register-users").view_name == "api:register-users"


def test_weather_data():
    assert reverse("api:weather-data") == "/api/weather-data"
    assert resolve("/api/weather-data").view_name == "api:get-data"
