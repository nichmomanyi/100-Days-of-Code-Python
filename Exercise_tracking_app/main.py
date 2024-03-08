import requests
from datetime import datetime as dt
import os

exercise_endpoint = os.environ["ENV_exercise_endpoint"]

EXERCISE_TEXT = input("Tell me which Exercise you did?")
APP_ID = os.environ["ENV_APP_ID"]
API_KEY = os.environ["ENV_API_KEY"]

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

exercise_param = {
    "query": EXERCISE_TEXT,
    "gender": "male",
    "weight_kg": "78",
    "height_cm": "163",
    "age": "29"
}

response = requests.post(exercise_endpoint, json=exercise_param, headers=headers)
result = response.json()
print(result)

################### Start of Step 4 Solution ######################

sheet_endpoint = os.environ["ENV_sheet_endpoint"]

Bearer_t = os.environ["ENV_Bearer_t"]

sheet_header = {
    "Authorization": Bearer_t
}

today_date = dt.now().strftime("%d/%m/%Y")
now_time = dt.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheet_header)

    print(sheet_response.text)
