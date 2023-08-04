# Developed by: Victor Chiemeka
# Date: 4/08/2023
# Description: Treasure Map Game: This program simulates a treasure map grid
# where the player can input a two-digit position to place a treasure on the grid.
# The grid is represented by a 3x3 matrix of empty spaces denoted by '⬜️'.
# After receiving the player's input, the program updates the grid and places an 'X' at the specified position, indicating the treasure's location. The updated grid is then displayed to show the treasure's placement.

# Define the initial 3x3 grid (matrix) with empty spaces represented by "⬜️"
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]

# Print the initial grid to show empty spaces
print(f"{row1}\n{row2}\n{row3}")

# Ask the user to input a position for the treasure
position = input("Where do you want to put the treasure? ")

# Extract the first digit as the column position and convert it to an integer
columnInput = int(position[0])

# Extract the second digit as the row position and convert it to an integer
rowInput = int(position[1])

# Update the selected position in the grid with "X" to place the treasure
map[rowInput - 1][columnInput - 1] = "X"

# Print the updated grid with the treasure placed at the specified position
print(f"{row1}\n{row2}\n{row3}")
