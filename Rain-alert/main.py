import requests
from twilio.rest import Client

parameter = {

    "lat": -1.284699,
    "lon": 36.733465,
    "appid": "b9e65fbc2cf46233de65110731e5e611",
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameter)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")
