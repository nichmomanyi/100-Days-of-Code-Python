import requests
import random

response = requests.get(url="https://kanye.rest/")
response.raise_for_status()

quote = response.json()
quote1 = random.choice(quote)
print(quote1)