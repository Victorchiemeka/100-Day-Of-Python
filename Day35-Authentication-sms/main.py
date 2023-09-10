import requests

# API key
API_KEY = "62d1ac921bd97546e6a839998a2bbd90"

# Latitude and longitude
latitude = 51.507351
longitude = -0.127758

# Endpoint
END_POINT = "https://api.openweathermap.org/data/2.5/onecall"

# Query parameters
parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": API_KEY,
}

# Make the API call
response = requests.get(END_POINT, params=parameters)

# Check the response status code
if response.status_code == 200:
    # Get the data
    data = response.json()

    # Print the hourly data
    print(data["hourly"])

else:
    print("Error:", response.status_code)
