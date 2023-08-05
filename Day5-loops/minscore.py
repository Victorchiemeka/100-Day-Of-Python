# Developed by: Victor Chiemeka
# Date: 5/08/2023
# Description: This program takes a list of student scores as input, finds the minimum score,
# and then prints the minimum score.

# Prompt the user to input a list of student scores separated by spaces.
student_scores = input("Input a list of student scores: ").split()

# Convert the input scores from strings to integers using a 'for' loop.
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Initialize the variable 'min_value' to the first score in the list.
min_value = student_scores[0]

# Iterate through the list of student scores to find the actual minimum score.
for num in student_scores:
    if num < min_value:
        min_value = num

# Print the minimum score.
print(f"The minimum value is: {min_value}")
