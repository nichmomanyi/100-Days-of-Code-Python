import requests
from twilio.rest import Client

account_sid = "AC39b6ca493feb968b2f527c00fd018bca"
auth_token = "3174e8c395e4aeeae0867b3813593c96"


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
    if int(condition_code) > 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is not going to rain today, don't carry an umbrella ☔︎︎",
        from_="+15134079698",
        to="+254715210571"
    )
    print(message.status)
