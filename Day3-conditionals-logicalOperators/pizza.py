# Developed by: Victor Chiemeka
# Date: 3/08/2023
# Description: This is a program that give the total output of pizza order
#  based on size and other thing u want to be added

print("Welcome to pizza delivery company")

pizza_size = input("What size do you want? S, M or L: ").capitalize()
add_pepper = input("Do you want to add pepper? Y or N:  ").capitalize()
extra_chesses = input("Do you want to add extra cheese? Y or N: ").capitalize()

price = 0

if pizza_size == "S":
    price = 15
    if add_pepper == "Y":
        price += 2
    if extra_chesses == "Y":
        price += 1
    print(f"Your final bill is {price}")

elif pizza_size == "M":
    price = 20
    if add_pepper == "Y":
        price += 3
    if extra_chesses == "Y":
        price += 1
    print(f"Your final bill is {price}")

elif pizza_size == "L":
    price  = 25
    if add_pepper == "Y":
        price += 3
    if extra_chesses == "Y":
        price += 1
    print(f"Your final bill is {price}")
