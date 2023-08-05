# Developed by: Victor Chiemeka
# Date: 5/08/2023
# Description: This program takes a list of student scores as input, finds the highest score,
# and then prints the highest score.

# Prompt the user to input a list of student scores separated by spaces.
student_scores = input("Input a list of student scores: ").split()

# Convert the input scores from strings to integers.
for n in range(len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Initialize the variable 'highest_score' to the first score in the list.
highest_score = student_scores[0]

# Iterate through the list of student scores to find the actual highest score.
for score in student_scores:
    if score > highest_score:
        highest_score = score

# Print the highest score.
print(f"The highest score is {highest_score}")
