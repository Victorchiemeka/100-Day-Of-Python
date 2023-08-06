import random

letters = [
    "a",
    "b",
    "c",
    # ... (the rest of the letters)
    "Y",
    "Z",
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

myTotal = []
for characters in range(0, nr_letters):
    myTotal += random.choice(letters)

for characters in range(0, nr_symbols):
    myTotal += random.choice(symbols)

for characters in range(0, nr_numbers):
    myTotal += random.choice(numbers)

random.shuffle(myTotal)  # Shuffle the password characters in place
password = ""
for char in myTotal:
    password += char

print(password)
