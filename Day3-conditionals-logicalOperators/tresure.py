# Developed by: Victor Chiemeka
# Date: 2/08/2023
# Description: This a game that check for user input and give an output based on the users input


print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Write your code below this line 👇
choice = input('Where do you want to go? Type "left" or "right" \n').lower()

if choice == "left":
    lake = input(
        'You have come to a lake.There is an island in the middle of the lake.Type "wait" to wait for boat.Type "swim" to swim across\n'
    )
    if lake == "wait":
        door = input(
            "You arrived at the island in the middle of the lake. There is a house with 3 doors. One red, One yellow and One blue. Which do you choose? \n"
        )
        if door == "yellow":
            print("You Win!")
        elif door == "blue":
            print("You entered the house of beast. Game over")
        elif door == "red":
            print("you have entered the house of whales")

        else:
            print("The house you entered does not exit")

    elif lake == "swim":
        print("You have been drowned, Game over.")
    else:
        print("Game over")
elif choice == "right":
    print("There is no lake here. Game Over")
else:
    print("Game Over")
