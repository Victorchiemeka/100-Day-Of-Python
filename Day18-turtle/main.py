import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Random Walk")
screen.bgcolor("white")

# Create the turtle
walker = turtle.Turtle()
walker.speed(0)  # Set the drawing speed (0 = fastest)

# Define the number of steps and step length
num_steps = 100
step_length = 20

# Perform the random walk
for _ in range(num_steps):
    # Generate a random angle between 0 and 360 degrees
    angle = random.uniform(0, 360)

    # Generate a random color
    random_color = (random.random(), random.random(), random.random())
    walker.pencolor(random_color)

    # Move the turtle forward in the specified direction
    walker.forward(step_length)
    walker.right(angle)

# Close the screen on click
screen.exitonclick()
