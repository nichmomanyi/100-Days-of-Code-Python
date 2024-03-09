import requests

destination_endpoint = "https://api.sheety.co/b6435ab822d11fc33c903cb8116f6d18/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(destination_endpoint)
        data = response.json()
        self.destination_data=data["prices"]
        return  self.destination_data
#         print(destination_data)
#
# DataManager().get_destination_data()


