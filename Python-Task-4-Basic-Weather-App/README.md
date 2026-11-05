#  Basic Weather Application

A simple and interactive Weather Application built using Python. This application allows users to search for any city and retrieve its current weather information using the free Open-Meteo API.

##  Features

- Search weather by city name.
- Display current temperature in Celsius.
- Show weather conditions.
- Display feels-like temperature.
- Show humidity percentage.
- Display wind speed.
- Show local date and time.
- Search weather for multiple cities.
- Handle invalid city names and network errors.

##  Technologies Used

- **Python** – Core programming language.
- **Requests** – To send HTTP requests and retrieve API data.
- **Open-Meteo API** – For weather forecasts and geocoding.
- **JSON** – To process API responses.

##  Project Structure

```text
Python-Task-4-Basic-Weather-App/
│
├── main.py
├── requirements.txt
└── README.md
```

##  Installation

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd Python-Task-4-Basic-Weather-App
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

##  How to Run

Execute the following command:

```bash
python main.py
```

Enter a city name to retrieve its current weather information.

##  Sample Output

```text
====================================
          WEATHER APPLICATION
====================================

Enter city name: Karachi

Fetching weather information...

====================================
          CURRENT WEATHER
====================================

City: Karachi
Country: Pakistan
------------------------------------
Temperature: 29.5 °C
Feels Like: 32.1 °C
Condition: Partly Cloudy
Humidity: 65%
Wind Speed: 14.2 km/h
------------------------------------

Thank you for using Weather Application!
```

*Note: Sample weather values are illustrative. Actual results depend on live API data.*

## 🌐 API Information

This project uses the free **Open-Meteo API**.

- Weather API: https://open-meteo.com/
- Geocoding API: https://open-meteo.com/en/docs/geocoding-api

No API key is required for this basic application.

## Learning Objectives

This project demonstrates practical implementation of:

- Python functions
- While loops and conditional statements
- Exception handling
- HTTP requests
- API integration
- JSON data handling
- Working with dictionaries
- User input validation

##  Author

Umm E Aeiman

Python Developer | AI Enthusiast

## License

This project is created for educational purposes as part of the OIBSIP Python Programming Internship.