# Weather Program

import requests
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

def get_weather(city):
    """Fetch the weather data for the given city."""
    api_key = os.getenv("OPENWEATHER_API_KEY")  # Load API key from environment variable
    if not api_key:
        print("API key not found. Please ensure it's defined in the .env file.")
        return None
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        
        data = response.json()
        if data["cod"] != 200:
            print(f"Error: {data['message']}")
            return None
        
        # Extracting relevant data from the response
        weather = {
            "city": city,
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather(weather):
    """Display the weather information."""
    if weather:
        print(f"\nWeather in {weather['city']}:\n")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Condition: {weather['condition']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Pressure: {weather['pressure']} hPa")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Unable to retrieve weather information.")

def main():
    print("Welcome to the Weather Program!")
    
    city = input("Enter the name of the city: ")
    
    weather = get_weather(city)
    display_weather(weather)

if __name__ == "__main__":
    main()
