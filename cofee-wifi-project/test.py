# Your list of cafes
cafes = [
    "Cafe Name,Location,Open,Close,Coffee,Wifi,Power",
    "Lighthaus,https://goo.gl/maps/2EvhB4oq4gyUXKXx9,11AM, 3:30PM,☕☕☕☕️,💪💪,🔌🔌🔌",
    "Esters,https://goo.gl/maps/13Tjc36HuPWLELaSA,8AM,3PM,☕☕☕☕,💪💪💪,🔌",
    "Ginger & White,https://goo.gl/maps/DqMx2g5LiAqv3pJQ9,7:30AM,5:30PM,☕☕☕,✘,🔌",
    "Mare Street Market,https://goo.gl/maps/ALR8iBiNN6tVfuAA8,8AM,1PM,☕☕,💪💪💪,🔌🔌🔌",
]

# Split the first element of the list and get the Cafe Name
first_row = cafes[0].split(",")[0]
# cafe_name = first_row[0]

print("Cafe Name:", first_row)
