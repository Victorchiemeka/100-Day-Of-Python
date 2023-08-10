# Developed by: Victor Chiemeka
# Date: 9/08/2023
# Description: A program that get the highest bidder from the input of the user

from art import logo

print(logo)


def clear_screen():
    print("\033c", end="")


diction = {}


#  A function to get the highest bidder
def highestbid(bidderscore):
    highest = 0
    winner = ""
    for bidder in bidderscore:
        bidder_amount = bidderscore[bidder]
        if bidder_amount > highest:
            highest = bidder_amount
            winner = bidder
    print(f"the winner is {winner} and the highest bid is {highest}")


def main():
    restart = True
    while restart:
        name = input("What is your name: ")
        price = int(input("What's your bid?: $"))
        diction[name] = price

        other = input("Are there other biders? 'yes' or 'no' ")
        if other == "yes":
            clear_screen()
            restart
        elif other == "no":
            highestbid(diction)
            # clear_screen()
            restart = False
        else:
            print("enter the correct input")
            restart = True


main()
