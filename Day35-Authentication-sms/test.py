import requests

# API key
API_KEY = "62d1ac921bd97546e6a839998a2bbd90"

# City name
city = "London"

# URL
url = (
    "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(
        city, API_KEY
    )
)

# Get response
response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:
    # Get the data
    data = response.json()

    # Get the longitude and latitude
    longitude = data["coord"]["lon"]
    latitude = data["coord"]["lat"]

    print("Longitude:", longitude)
    print("Latitude:", latitude)
    print(data)

else:
    print("Error:", response.status_code)
