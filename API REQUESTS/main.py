import requests
from datetime import datetime

TOKEN = "gjfdkwkkffj"
USERNAME = "nich254"
GRAPHID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_param = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(graph_endpoint, json=graph_param, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPHID}"

date = datetime.today()
updated_date = date.strftime("%Y%m%d")
print(updated_date)

pixel_param = {
    "date": updated_date,
    "quantity": input("How many kilometres did you run today?")
}

# response = requests.post(pixel_endpoint, json=pixel_param, headers=headers)
# print(response.text)

# UPDATING
pixel_update_endpoint = f"{pixel_endpoint}/{updated_date}"

updated_pixel = {
    "quantity": "36"
}

response = requests.put(pixel_update_endpoint, json=updated_pixel, headers=headers)
print(response.text)

# # Deleting
# pixel_delete_endpoint = f"{pixel_endpoint}/{updated_date}"
#
# response = requests.delete(pixel_delete_endpoint, headers=headers)
# print(response.text)