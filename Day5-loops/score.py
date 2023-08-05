# Developed by: Victor Chiemeka
# Date: 5/08/2023
# Description: This program calculates the squares of the numbers in a given list and stores them in a new list.

# Create the input list with five numbers: 2, 3, 5, -2, and 10.
list = [2, 3, 5, -2, 10]

# Initialize an empty list called 'squareList', which will store the squares of the numbers.
squareList = []

# Loop through each element 'i' in the 'list'.
for i in list:
    # Calculate the square of the current element and assign it to the variable 'square'.
    square = i**2

    # Append the square value to the 'squareList' using the 'append()' method.
    squareList.append(square)

# Print the 'squareList', which contains the squares of the numbers from the original list.
print(squareList)
