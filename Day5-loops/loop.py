# Developed by: Victor Chiemeka
# Date: 5/08/2023
# Description: This program takes a list of student heights as input, calculates the average height,
# and then prints the rounded average.

# Prompt the user to input a list of student heights separated by spaces.
student_heights = input("Input a list of student heights: ").split()

# Convert the input heights from strings to integers.
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Initialize the variable 'total' to 0. This variable will be used to store the sum of all student heights.
total = 0

# Calculate the sum of all student heights using a 'for' loop.
for height in student_heights:
    total += height

# Initialize the variable 'count' to 0. This variable will be used to store the number of students (i.e., the number of height values in the list).
count = 0

# Calculate the total number of students by iterating through the list of student heights using a 'for' loop.
for length in student_heights:
    count += 1

# Calculate the average height by dividing the 'total' sum of heights by the 'count' (number of students).
final = total / count

# Print the average height after rounding it to the nearest integer.
print(round(final))
