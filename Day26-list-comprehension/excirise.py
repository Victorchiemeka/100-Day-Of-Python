weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
# for my in weather_c:
#     print(my,weather_c[my])
# Write your code 👇 below:
weather_f = {my: weather_c[my] * 9 / 5 + 32 for my in weather_c}

print(weather_f)
