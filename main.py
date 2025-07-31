import requests
from dotenv import load_dotenv
import os
load_dotenv()

OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric'  
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            main_weather = data['weather'][0]['main']
            description = data['weather'][0]['description']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            
            print(f"\nWeather in {city.title()}:")
            print(f"  Condition: {main_weather} ({description})")
            print(f"  Temperature: {temp}°C")
            print(f"  Humidity: {humidity}%")
            
        else:
            print(f"Error: Could not find weather for '{city}'. Please check the city name.")

    except requests.exceptions.RequestException:
        print("Error: Could not connect to the weather service. Please check your internet connection.")


if __name__ == "__main__":
    print(OPENWEATHER_API_KEY)
    
    print("""
\tWelcome to the Weather App
----------------------------------------------
        """)
    city = input("Enter the city name: ")
    
    if city.strip():
        get_weather(city)
    else:
        print("Error: Please enter a valid city name.")