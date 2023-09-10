import requests
from datetime import datetime


GENDER = "MALE"
WEIGHT_KG = "60"
HEIGHT = "160.5"  # entered random height in cm
AGE = "50"

APP_ID = "fc02fae1"
API_KEY = "b938e9b0dd2c6a304ae5c8a89592635e"  # Remove the extra character here
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = (
    "https://api.sheety.co/a1b4f8011617c0d163bc6e8244584a22/workoutTracking/workouts"
)

exercise_input = input("Tell which exercise you did today?: ")

# Update the headers with the correct keys
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)

result = response.json()
exercise_name = result["exercises"][0]["name"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]
current_date = datetime.now()
# Format the date as "dd/mm/yyyy"
formatted_date = current_date.strftime("%d/%m/%Y")

# Get the current time
current_time = datetime.now().time()

# Get the current seconds
current_seconds = current_time.second

# Round the seconds to the nearest two-digit number
rounded_seconds = (current_seconds + 1) if current_seconds < 59 else 0

# Format the time as "hh:mm:ss"
formatted_time = current_time.replace(second=rounded_seconds).strftime("%H:%M:%S")
now_time = datetime.now().strftime("%X")

headers = {"Authorization": "Bearer Vitaosecrettoken"}


new_row_data = {
    "workout": {
        "date": formatted_date,
        "time": now_time,
        "exercise": exercise_name.title(),
        "duration": duration,
        "calories": calories,
    }
}


response = requests.post(url=sheety_endpoint, json=new_row_data, headers=headers)
# Check the response
