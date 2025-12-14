from weather import get_weather

def main():
    city = input("Enter a city: ")

    weather_data, error = get_weather(city)

    if error:
        print(f"❌ Error: {error}")
        return

    location = weather_data["location"]["name"]
    condition = weather_data["current"]["condition"]["text"]
    temp_f = weather_data["current"]["temp_f"]
    humidity = weather_data["current"]["humidity"]
    wind = weather_data["current"]["wind_mph"]

    print(f"\nWeather Summary for {location}:\n")
    print(f"Condition: {condition}")
    print(f"Temperature: {temp_f}°F")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} mph")

if __name__ == "__main__":
    main()
