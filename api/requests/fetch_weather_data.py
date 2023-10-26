import os
import logging

import requests
from marshmallow import ValidationError

from api.schemas.WeatherForecast import WeatherForecast

# Get the secret key from the environment
if os.environ.get("GITHUB_ACTIONS"):
    weather_api_key = os.environ.get("WEATHER_API_KEY")  # GitHub Secret
else:
    from dotenv import load_dotenv

    load_dotenv()  # Load local .env file
    weather_api_key = os.environ.get("WEATHER_API_KEY")  # Local Secret

base_url = "http://api.weatherapi.com/v1/forecast.json"


def fetch_weather_data():
    """
    Fetches the latest weather forecast from the Weather API. - Raw data

    Returns:
        dict: A dictionary containing the latest weather forecast from the
        Weather API in JSON format.
    """
    params = {"key": weather_api_key, "q": "64152", "days": 3}

    response = requests.get(base_url, params=params)
    res_data = response.json()

    if response.status_code != 200:
        raise Exception(
            f"Unable to fetch weather data: {res_data.code}-{res_data.message}"
        )

    return res_data


def validate_weather_data(data):
    """
    Validates the weather data returned by the Weather API.

    Args:
        data (dict): A dictionary containing the Weather forecast objects from
        the Weather API in JSON format.

    Returns:
        dict: A dictionary of validated Weather objects.
    """
    try:
        validated_data = WeatherForecast().load(data)
        return validated_data
    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return {}


def convert_weather_data_to_dict():
    """
    Converts the weather data returned by the Weather API to a dictionary.

    Args:
        data (dict): A dictionary containing the Weather forecast objects from
        the Weather API in JSON format.

    Returns:
        dict: A dictionary containing the weather forecast data.
    """
    try:
        data = fetch_weather_data()
        logging.info(data)
        logging.info(validate_weather_data(data))  
        return validate_weather_data(data)
    except Exception as err:
        logging.error(f"Failed to fetch and validate weather data: {err}")
        return {}
