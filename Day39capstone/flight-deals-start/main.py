# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager

ORIGIN_CITY_IATA = "LON"
mydata = DataManager()  # create an instance of DataManager
sheet_data = mydata.Get()
# call the Get method and assign its return value to sheet_data
# pprint(sheet_data)  # print sheet_data using pprint


if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

        print(f"sheet_data:\n {sheet_data}")

        mydata.destination_data = sheet_data
        mydata.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
