# import csv

# with open("./weather_data.csv") as file:
#     data = csv.reader(file)
#     temp = []
#     for new in data:
#         if new[1] != "temp":
#             temp.append(int(new[1]))

# print(temp)

import pandas

data = pandas.read_csv("weather_data.csv")
mydata = data.to_dict()
#print(mydata)

my_list = data["temp"].to_list()
#print(my_list)

firstday = data[data["day"] == "Monday"]

celsuis = firstday.temp[0] * 9/5 + 32
print(celsuis)
