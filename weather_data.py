import requests
import json
from datetime import datetime

def get_weather_data_shirur():
    # WeatherAPI.com configuration
    API_KEY = "36c51f6fbacf4b3498c31144252707"
    # Shirur, Pune coordinates
    LAT = "18.8333"
    LON = "74.3333"
    
    # API endpoint for current weather and forecast
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={LAT},{LON}&days=2&aqi=no"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Get current day's rainfall
        current_day_rain = data['forecast']['forecastday'][0]['day']['totalprecip_mm']
        # Get last 3 hours rainfall (approximation from hourly data)
        current_hour = datetime.now().hour
        last_3h_rain = sum(
            hour['precip_mm'] 
            for hour in data['forecast']['forecastday'][0]['hour']
            if current_hour - 3 <= int(hour['time'].split()[1].split(':')[0]) <= current_hour
        )
        
        # Get tomorrow's forecasted rainfall
        tomorrow_rain = data['forecast']['forecastday'][1]['day']['totalprecip_mm']
        
        return {
            'current_24h_rain': current_day_rain,
            'current_3h_rain': last_3h_rain,
            'tomorrow_24h_rain': tomorrow_rain
        }
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        # Return default values if API fails
        return {
            'current_24h_rain': 0,
            'current_3h_rain': 0,
            'tomorrow_24h_rain': 0
        }

# Shirur specific soil and terrain information
SHIRUR_INFO = {
    'soil_type': 'clay',  # Predominant soil type in Shirur
    'slope_degrees': 35,   # Average slope in the region
    # Note: These are placeholder values, should be updated with actual data
    'soil_moisture_pct': 35,  # To be replaced with sensor data
    'pore_water_pressure_kpa': 15  # To be replaced with sensor data
}
