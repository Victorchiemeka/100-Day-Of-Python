# Developed by: Victor Chiemeka
# Date: 4/08/2023
# Description:A program that generates random number between 0 and 1
# and prints 'Head' if randomNumber is 1 and Tails if zero

import random

test = int(input("Enter a number: "))
random.seed(test)

randomNumber = random.randint(0, 1)
if randomNumber == 1:
    print("Heads")
else:
    print("Tails")
