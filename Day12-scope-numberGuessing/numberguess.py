import random
from art import logo

print(logo)


# Print welcome
def welcome():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def random_number():
    total = random.randint(1, 100)
    return total


welcome()
EASY = 10
HARD = 5
game_mode = input("Choose a difficulty. Type 'easy' or hard:")
generate_number = random_number()

if game_mode == "easy":
    print(f"You have {EASY} attempt remaining to guess the number")
    restart = True
    while restart:
        guess = int(input("Make a guess: "))
        if guess > generate_number:
            print("Too High ")
            print("Guess again")
            EASY = EASY - 1
            print(f"You have {EASY} attempt remaining to guess the number")
        elif guess < generate_number:
            print("Too low ")
            print("try again")
            EASY = EASY - 1
            print(f"You have {EASY} attempt remaining to guess the number")
        elif guess == generate_number:
            print(f"You got it! the answer was {generate_number}")
            restart = False
        if EASY < 1:
            if guess > generate_number:
                print("Too high ")
                print("You've run out of guesses")
            elif guess < generate_number:
                print("Too low ")
                print("You've run out of guesses")
            restart = False

elif game_mode == "hard":
    print(f"You have {HARD} attempt remaining to guess the number")
    restart = True
    while restart:
        guess = int(input("Make a guess: "))
        if guess > generate_number:
            print("Too high ")
            print("Guess again")
            HARD = HARD - 1
            print(f"You have {HARD} attempt remaining to guess the number")
        elif guess < generate_number:
            print("Too low ")
            print("try again")
            HARD = HARD - 1
            print(f"You have {HARD} attempt remaining to guess the number")
        elif guess == generate_number:
            print(f"You got it! the answer was {generate_number}")
            restart = False
        if HARD < 1:
            if guess > generate_number:
                print("Too high ")
                print("You've run out of guesses")
            elif guess < generate_number:
                print("Too low ")
                print("You've run out of guesses")
            restart = False
