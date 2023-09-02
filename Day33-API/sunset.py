import requests
from datetime import datetime

MY_LAT = 6.524379
MY_LONG = 3.379206


parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        }

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
#print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T")[1].split(":"))

