# Developed by: Victor Chiemeka
# Date: 5/08/2023
# Description: add 1 to 100 and print out the outcome.

# Initialize the 'total' variable to 0. This variable will be used to store the sum of numbers from 1 to 100.
total = 0

# Loop through numbers from 1 to 100 using the 'range' function.
for i in range(1, 101):
    # Add the current number 'i' to the 'total' variable in each iteration.
    total += i

# Print the final sum of numbers from 1 to 100.
print(total)
