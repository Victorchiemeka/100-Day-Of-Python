# Developed by: Victor Chiemeka
# Date: 5/08/2023
# Description: This program prints numbers from 1 to 100. For multiples of 3, it prints "Fizz",
# for multiples of 5, it prints "Buzz", and for numbers that are multiples of both 3 and 5, it prints "FizzBuzz".

# Loop through numbers from 1 to 100 using the 'range' function.
for i in range(1, 101):
    # Check if the number is divisible by both 3 and 5.
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Check if the number is divisible by 3.
    elif i % 3 == 0:
        print("Fizz")
    # Check if the number is divisible by 5.
    elif i % 5 == 0:
        print("Buzz")
    # If the number is not divisible by 3 or 5, simply print the number itself.
    else:
        print(i)
