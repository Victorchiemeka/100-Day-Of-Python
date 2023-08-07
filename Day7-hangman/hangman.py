import random
import hangman_art
import hangman_word


def hangman_game():
    # Get a random word from the word list
    word = hangman_word.word_list
    get_rand = random.choice(word)

    # Initialize the display list with underscores to represent the hidden word
    display = ["_" for _ in get_rand]

    # Set the number of lives the player has
    lives = 6

    # Flag to check if the game has ended
    endOfgame = False

    # Load ASCII art and stages for the hangman
    art = hangman_art.logo
    theArt = hangman_art.stages
    print(art)

    # Main game loop
    while not endOfgame:
        # Get player input (a single letter)
        askInput = input("\nEnter a letter: ").lower()

        # Check if the letter is in the random word
        if askInput in get_rand:
            # Replace underscores in the display list with the correct letter
            for index, letter in enumerate(get_rand):
                if letter == askInput:
                    display[index] = askInput
        else:
            # The letter is not in the word, decrement lives
            lives -= 1
            if lives == 0:
                # Player has run out of lives, end the game
                endOfgame = True
                print("You lose.")

        # Display the current state of the word (with hidden letters)
        print(" ".join(display))

        # Check if all letters are revealed (no underscores remaining)
        if "_" not in display:
            # All letters are revealed, player wins
            endOfgame = True
            print("You win")

        # Display the current state of the hangman based on the remaining lives
        print(theArt[lives])


def main():
    # Call the hangman_game function to play the game
    hangman_game()


if __name__ == "__main__":
    # Start the game by calling the main function
    main()
