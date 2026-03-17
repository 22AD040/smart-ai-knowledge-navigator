from utils.api_utils import get_weather

def weather_insight(city):

    data=get_weather(city)

    insight=f"""
Temperature: {data['temp']}°C
Humidity: {data['humidity']}%
Condition: {data['description']}

AI Advice:
Stay hydrated and plan activities accordingly.
"""

    return insight