# Developed by: Victor Chiemeka
# Date: 8/08/2023
# Description:A program that appends a new value into a list of dictionary

travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]


def add_new_country(country, number, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visit"] = number
    new_country["cities"] = cities
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# for country in travel_log:
#     country["country"] = "Russia"
#     country["visits"] = 2
#     country["cities"] = ["Moscow", "Saint Petersburg"]
#     print(country["country"], country["visits"], country["cities"])

# print(travel_log)
