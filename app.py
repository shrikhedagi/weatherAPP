import requests

# Define the endpoint and your API key
url = "https://api.openweathermap.org/data/2.5/weather"
api_key = "ad87425ade0f2053cabddf01c26d21af"  # Your actual API key

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def display_weather(data):
    if data:
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Error fetching weather data. Please check the city name and try again.")

def main():
    city_name = input("Enter the name of the city or town: ")
    weather_data = get_weather(city_name)
    display_weather(weather_data)

if __name__ == "__main__":
    main()






