import os

import requests
from twilio.rest import Client

API_KEY = os.environ["owm_api_key"]
OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
ACCOUNT_SID = os.environ["account_sid"]
AUTH_TOKEN = os.environ["auth_token"]
MY_LAT = 59.938480
MY_LON = 30.312481

parameters = {"appid": API_KEY,
              "lat": 56.838924,
              "lon": 60.605701,
              "lang": "ru",
              "exclude": "current,minutely,daily,alerts",
              "units": "metric",
              }
response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
for i in range(12):
    if weather_data["hourly"][i]["weather"][0]["id"] < 700:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
            body="На улице дождь, возьми зонт.",
            from_='+15312344611',
            to='+358449181656'
        )
        print(message.status)
        break
