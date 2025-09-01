import os
import requests
from datetime import datetime

app_id = os.getenv("Nutritionix_APP_ID")
api_key = os.getenv("Nutritionix_API_KEY")
sheety_token = os.getenv("Sheety_TOKEN")


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/9c28b8e3a3d0a3989daf443af364a53d/myWorkout/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}

parameters = {
    "query": exercise_text,
    "gender": "female",
    "weight_kg": 80,
    "height_cm": 175,
    "age": 20
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
exercises = response.json()["exercises"]

for exercise in exercises:
    workout_data = {
        "workout": {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_headers = {
        "Authorization": f"Bearer {sheety_token}",
        "Content-Type": "application/json"
    }

    sheety_response = requests.post(sheety_endpoint, json=workout_data, headers=sheety_headers)

    # for testing
    print(sheety_response.text)
