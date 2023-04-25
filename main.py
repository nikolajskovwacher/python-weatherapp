import requests
import json

# API key
with open("apikey.txt", "r") as file:
    _apikey = file.read()

# Response handling
def build_output(weather_data):
    # Extract some key information
    location_name = weather_data["location"]["name"]
    temperature_c = weather_data["current"]["temp_c"]
    condition_text = weather_data["current"]["condition"]["text"]
    # Print the extracted information
    print("Location:", location_name)
    print("Temperature:", temperature_c, "°C")
    print("Condition:", condition_text)

# Building API call
def api_call_builder(apikey, location):
    api_call = f"http://api.weatherapi.com/v1/current.json?key={apikey}&q={location}&aqi=no"
    return api_call

# User input and API call
_location = input("Where would you like to know the current weather?: ")
response = requests.get(api_call_builder(_apikey, _location))

if response.status_code == 200:
    data = json.loads(response.text)
    build_output(data)
else:
    print('Error fetching weather information.')