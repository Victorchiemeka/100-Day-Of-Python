# Developed by: Victor Chiemeka
# Date: 2/08/2023
# Description:  calculates the number of days, weeks, and months left until the user reaches the age of 90

age = int (input("What is your current age? "))

remaining_years = 90 - age
days_remaining = remaining_years * 365
weeks_remaining = remaining_years * 52
month_remaining = remaining_years * 12

message = f"you have {days_remaining} days , {weeks_remaining} weeks and {month_remaining} months left"
print(message)