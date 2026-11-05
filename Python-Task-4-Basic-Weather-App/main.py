
import requests

print("====================================")
print("          WEATHER APPLICATION")
print("====================================")

# Weather condition descriptions
weather_conditions = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing Rime Fog",
    51: "Light Drizzle",
    53: "Moderate Drizzle",
    55: "Dense Drizzle",
    61: "Slight Rain",
    63: "Moderate Rain",
    65: "Heavy Rain",
    71: "Slight Snow",
    73: "Moderate Snow",
    75: "Heavy Snow",
    80: "Rain Showers",
    81: "Moderate Rain Showers",
    82: "Violent Rain Showers",
    95: "Thunderstorm",
    96: "Thunderstorm with Hail",
    99: "Heavy Thunderstorm with Hail"
}


def get_weather(city):

    try:
        # Step 1: Find city coordinates

        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geo_url,
            params=geo_params,
            timeout=15
        )

        geo_response.raise_for_status()

        geo_data = geo_response.json()

        if not geo_data.get("results"):
            print("\nCity not found! Please try another city.")
            return

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        city_name = location["name"]
        country = location.get("country", "Unknown")

        # Step 2: Get current weather

        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "apparent_temperature,"
                "weather_code,"
                "wind_speed_10m"
            ),
            "timezone": "auto"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=15
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()

        current = weather_data["current"]

        # Step 3: Extract weather information

        temperature = current["temperature_2m"]
        feels_like = current["apparent_temperature"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]
        weather_code = current["weather_code"]

        condition = weather_conditions.get(
            weather_code,
            "Unknown Weather Condition"
        )

        local_time = current["time"]

        # Step 4: Display weather report

        print("\n====================================")
        print("          CURRENT WEATHER")
        print("====================================")

        print(f"City: {city_name}")
        print(f"Country: {country}")
        print("------------------------------------")

        print(f"Temperature: {temperature} °C")
        print(f"Feels Like: {feels_like} °C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")

        print("------------------------------------")
        print(f"Local Date & Time: {local_time}")

        print("====================================")

    except requests.exceptions.Timeout:
        print("\nError: Request timed out. Try again.")

    except requests.exceptions.ConnectionError:
        print("\nError: Please check your internet connection.")

    except requests.exceptions.HTTPError:
        print("\nError: Unable to retrieve weather information.")

    except requests.exceptions.RequestException as error:
        print(f"\nNetwork Error: {error}")

    except (KeyError, IndexError, TypeError, ValueError):
        print("\nError: Unexpected weather data received.")


# Step 5: Main application loop

while True:

    city = input("\nEnter city name: ").strip()

    if not city:
        print("Please enter a valid city name.")
        continue

    print("\nFetching weather information...")

    get_weather(city)

    again = input(
        "\nDo you want to check another city? (yes/no): "
    )

    if again.lower().strip() != "yes":

        print("\nThank you for using Weather Application!")
        break
