# Developed by: Victor Chiemeka
# Date: 2/08/2023
# Description: This program checks if year is leap year

print("Welcome to love calculator")

firstLove = input("What is your name: ").lower()
secondLove = input("What is their name: ").lower()

combineName = firstLove + secondLove

t = combineName.count("t")
r = combineName.count("r")
u = combineName.count("u")
e = combineName.count("e")

true = t + r + u + e

l = combineName.count("l")
o = combineName.count("o")
v = combineName.count("v")
e = combineName.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos.")

elif (love_score <= 40) or (love_score > 90):
    print(f"Your score is {love_score}, you are alright.")

else:
    print(f"Your score is {love_score}, you are alright.")
