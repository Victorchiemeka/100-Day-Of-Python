# from turtle import *

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# myscreen = Screen()
# print(myscreen.canvheight)
# myscreen.exitonclick()

from prettytable import PrettyTable


x = PrettyTable()
x.field_names = [
    "Pokemon Name",
    "Type",
]
x.add_row(["Pikachu", "Electric"])
x.add_row(["Squirtle", "Water"])
x.add_row(["Charamandar", "Fire"])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])
print(x)
