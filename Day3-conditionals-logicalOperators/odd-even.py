# Developed by: Victor Chiemeka
# Date: 3/08/2023
# Description: This program checks if a number is odd or even using modular operator

# getting the users input and converting to an int 
number = int(input("What number do you want to check? "))

# Check if user input divided by 2 is equal to zero
if (number % 2 == 0):
    # printing out this output to the user
    print("this is an even number")

# a condition that check if the user input divided by two has a remainder
else:
    # printing out this output to the user
    print("this is an odd number ")