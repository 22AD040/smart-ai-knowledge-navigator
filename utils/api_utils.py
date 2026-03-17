import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):

    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_KEY}&units=metric"

    res=requests.get(url).json()

    return {
        "temp":res["main"]["temp"],
        "humidity":res["main"]["humidity"],
        "description":res["weather"][0]["description"]
    }