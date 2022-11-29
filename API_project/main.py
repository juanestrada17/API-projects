import time

import requests
import smtplib
from datetime import datetime

MY_LAT = 6.090000
MY_LONG = -75.636630


# TODO 1 creates the function to check if the ISS is close|overhead
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude <= MY_LONG + 5:
        return True


# TODO 2 creates the function to check if it's dark

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 5
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 5

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


# TODO 3 sends the email and runs the program every 60 seconds to see if it's nearby

my_email = "testinmail17@gmail.com"
password = "testers17"

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="juanzatch17@hotmail.com",
                            msg=f"Subject: ISS LOCATION NEAR!\n\n Please look up! ISS LOCATION NEAR!")

