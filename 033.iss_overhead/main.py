import smtplib
import time
from datetime import datetime
import requests

MY_EMAIL = "rutkovskiileonid@gmail.com"
MY_PASSWORD = "kfczavmjooajtwfr"


def send_letter():
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:Look UP!\n\nLook Up, ISS is here."
    )


MY_LAT = 59.938480
MY_LONG = 30.312481


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if 5 >= (MY_LAT - iss_latitude) >= -5 and 5 >= (MY_LONG - iss_longitude) >= -5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if 24 > time_now > sunset or sunrise > time_now > 0:
        return True


while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        send_letter()
