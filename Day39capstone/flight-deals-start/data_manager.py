import requests
from pprint import pprint

SHEETY_ENDPOINT = (
    "https://api.sheety.co/a1b4f8011617c0d163bc6e8244584a22/copyOfFlightDeals/prices"
)


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination = {}

    def Get(self):
        response = requests.get(
            "https://api.sheety.co/a1b4f8011617c0d163bc6e8244584a22/copyOfFlightDeals/prices"
        )
        data = response.json()
        self.destination = data["prices"]
        return self.destination

    def update_destination_codes(self):
        for mycity in self.destination:
            new_data = {"price": {"iataCode": mycity["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{mycity['id']}", json=new_data
            )
            print(response.text)
