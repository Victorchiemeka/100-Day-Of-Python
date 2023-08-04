# Developed by: Victor Chiemeka
# Date: 4/08/2023
# Description: Users input names separated by commas. The program uses random selection to choose a person who treats everyone.
# Adds fairness and fun to gatherings or events
# Import the 'random' module to use random number generation
import random

# Ask the user for the number of names they want to provide
test_speed = int(input("Give everyone a name: "))

# Seed the random number generator with the provided number to ensure consistent randomness
random.seed(test_speed)

# Ask the user to input names separated by commas and split them into a list called 'name'
nameAs = input("Give me everyone's name, separated by commas: ")
name = nameAs.split(", ")

# Generate a random number between 0 and the number of names in the list
randomNumber = random.randint(0, len(name) - 1)

# Display the randomly selected name who will buy the meal
print(f"{name[randomNumber]} is going to buy the meal")
