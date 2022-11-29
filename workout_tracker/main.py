import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

user = "haseo17"
password = "sheety17"
APP_ID = "e661605b"
API_KEY = "1c2e12e2d70739ed37b06dda53f8f781"

minutes = input("How many minutes did you exercise today: ")
minute_params = {"query": f"{minutes}"}

headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}

URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=URL, json=minute_params, headers=headers)
result = response.json()
index = 0

# Sheety
#
today = datetime.now()

day = today.day
month = today.month
year = today.year

# USES strftime to show the date in the expected day/month/year
today_date = today.strftime('%d/%m/%Y')
time_hour = today.strftime("%H:%M:%S")

URL = 'https://api.sheety.co/e12dffbd339c4db2c12af9be98f2ef86/workoutTracking/workouts'

while len(result["exercises"]) > index:
    exercise = result["exercises"][index]['name']
    duration = result["exercises"][index]['duration_min']
    calories_burnt = result["exercises"][index]["nf_calories"]
    sheety_params = {
        "workout": {
            "date": f"{today_date}",
            "time": f"{time_hour}",
            "exercise": f"{exercise.title()}",
            "duration": f"{duration}",
            "calories": f"{calories_burnt}"
        }
    }
    response = requests.post(url=URL, json=sheety_params, auth=HTTPBasicAuth("user", "password"))
    index += 1

