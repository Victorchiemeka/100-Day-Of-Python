import requests
from datetime import datetime

# Constants
GENDER = "MALE"
WEIGHT_KG = "60"
HEIGHT = "160.5"  # entered random height in cm
AGE = "50"

APP_ID = "fc02fae1"
API_KEY = "b938e9b0dd2c6a304ae5c8a89592635e"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/a1b4f8011617c0d163bc6e8244584a22/workoutTracking/workouts"

# Input
exercise_input = input("Tell which exercise you did today?: ")

# Nutritionix API Request
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}
response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# Extract Exercise Data
exercise_data = result["exercises"][0]
exercise_name = exercise_data["name"]
duration = exercise_data["duration_min"]
calories = exercise_data["nf_calories"]

# Current Date and Time
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime('%d/%m/%Y %H:%M:%S')

# Prepare Row Data
new_row_data = {
    "date": formatted_datetime,
    "Exercise": exercise_name.title(),
    "Duration (min)": duration,
    "Calories Burned": calories,
}

# Add Row to Sheety
load_data = {
    "workouts": new_row_data
}

response = requests.post(url=sheety_endpoint, json=load_data)

# Check the response
if response.status_code == 201:
    print("New row added successfully.")
else:
    print(f"Failed to add a new row. Status code: {response.status_code}")

print(f"Exercise name: {exercise_name}, Duration: {duration} minutes, Calories: {calories}")

