# Developed by: Victor Chiemeka
# Date: 3/08/2023
# Description: This is a program that checks your height and uses a condition to know your required output

print("Welcome to the rollercoaster")

# asking the user to input height
height = int (input("What is your height in cm? "))
bill = 0
# check if height is greater than 120
if height >= 120:
    print("You can ride the rollercoaster")
    user_age = int(input("What is your age? "))
    if user_age <= 12:
        bill = 5 
        print("Child tickets are $5")
    
    elif user_age <= 18:
        bill = 8
        print("Youth ticket are  $8")
    else:
        bill = 12
        print("Youth ticket $12.")
    want_photo = input("Do you want to take a photo? Y or N. ")
    if want_photo == "Y":
        bill += 3
    print(f"Your total bills are {bill}")
else:
    print("You have to grow taller to ride the rollercoaster")