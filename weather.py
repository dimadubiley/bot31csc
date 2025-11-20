import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')


def get_weather(city: str) -> dict:
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return f"The weather in {city.capitalize()} is: {response.json()['main']['temp']}"

