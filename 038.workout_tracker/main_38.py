import datetime as dt
import os

import requests

APP_ID = os.environ["nutritionix_api_id"]
API_KEY = os.environ["nutritionix_api_key"]

GENDER = "FEMALE"
WEIGHT_KG = "63"
HEIGHT = "168"
AGE = "32"
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
AUTHORIZATION_HEADER = os.environ["auth_header"]
sheety_headers = {
    "Authorization": AUTHORIZATION_HEADER
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ["sheet_endpoint"]
exercise_input = input("Tell which exercise you did today?: ")
parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}
now = dt.datetime.now()
current_date = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
data = response.json()

exercises = data["exercises"]
workout = {}

for i in range(len(exercises)):
    workout = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercises[i]["name"].title(),
            "duration": exercises[i]["duration_min"],
            "calories": exercises[i]["nf_calories"],
        }
    }

    new_response = requests.post(SHEET_ENDPOINT, json=workout, headers=sheety_headers)
    print(new_response.text)
