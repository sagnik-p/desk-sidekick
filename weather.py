import requests
import json

# Replace with your OpenWeatherMap API key
api_key = #hidden for screen recording

# Specify the city name and optionally the country code
city_name = 'Kolkata'
country_code = 'IN'  # For example, 'US' for the United States

# Construct the API URL
base_url = 'http://api.openweathermap.org/data/2.5/weather'
params = {
    'q': f'{city_name},{country_code}',
    'appid': api_key,
    'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
}

# Make the API request
response = requests.get(base_url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    # Extract relevant weather information
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    print(f'Weather in {city_name}: {weather_description}')
    print(f'Temperature: {temperature}°C')
    print(f'Humidity: {humidity}%')
else:
    print(f'Failed to retrieve weather data. Status code: {response.status_code}')
