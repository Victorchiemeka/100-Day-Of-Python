# Developed by: Victor Chiemeka
# Date: 6/08/2023
# Description: a program that prints vitao based on the number of word the user inputted


def main():
    meow()


def meow():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break
    for _ in range(n):
        print("Vitao")


main()
