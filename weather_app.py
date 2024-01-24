import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # Change units to "imperial" for Fahrenheit

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            print(f"Weather in {city}: {temperature}°C, {description}")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key
    city = input("Enter the city name: ")
    get_weather(api_key, city)

if __name__ == "__main__":
    main()
