import requests
from twilio.rest import Client

api_key = OWM_API_KEY
OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
account_sid = 'AC2e2e35368f3a999033b5c3cc475a5aca'
auth_token = '481b73bc907faea70d35e133d792f7a7'
MY_LAT = 59.938480
MY_LON = 30.312481

parameters = {"appid": api_key,
              "lat": 56.838924,
              "lon": 60.605701,
              "lang": "ru",
              "exclude": "current,minutely,daily,alerts",
              "units": "metric",
              }
response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
for i in range(12):
    if weather_data["hourly"][i]["weather"][0]["id"] < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="На улице дождь, возьми зонт.",
            from_='+15312344611',
            to='+358449181656'
        )
        print(message.status)
        break
