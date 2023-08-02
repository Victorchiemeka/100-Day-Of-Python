# Developed by: Victor Chiemeka
# Date: 2/08/2023
# Description: is a simple tip calculator.

# Program Greetings
print("Welcome to the tip calculator")

# asking the user for necessary inputs
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? $"))
split = int(input("How many people to split the bill? "))

# getting the percentage to tip and adding to the bill
total = (percentage / 100) * bill + bill

# dividing the total bill with the number of people to split
totalBill = total / split
# using the round function to get two decimal places 
finalAmount = round(totalBill, 2)

# using a formatted string to get final output 
print(f"Each person should pay ${finalAmount}")