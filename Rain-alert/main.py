import requests

parameter = {

    "lat": -1.284699,
    "lon": 36.733465,
    "appid": "b9e65fbc2cf46233de65110731e5e611"
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameter)
data = response.json()
print(data)
