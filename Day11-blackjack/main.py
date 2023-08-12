import random
from art import logo


def clear_screen():
    print("\033c", end="")


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "Lose, opponent has a blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_blackjack():
    user_cards = []
    computer_cards = []

    # Deal initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Display user's current hand and score
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for game end conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_decision = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_decision == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

        # Computer's turn
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    # Display final hands and compare scores
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))


# Start the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear_screen()
    print(logo)
    play_blackjack()
