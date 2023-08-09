from art import logo

print(logo)
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


# main function
def main():
    restart = True
    # repeat the process
    while restart:
        # ask user for direction
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        # get a the users message and convert to lowercase
        text = input("Type your message:\n").lower()
        # get the input of the number you want the text to be shifted to
        shift = int(input("Type the shift number:\n"))
        # check if direction is "encode"
        if direction == "encode":
            # run the encrypt function
            encrypt(text, shift)
        # check if direction is "decode"
        elif direction == "decode":
            # run the decode function
            decrypt(text, shift)
        # take input of yes or no
        starter = input('Type "yes" if you want to go again.Otherwise "no" ')
        # if the input is "yes continue the forever loop"
        if starter == "yes":
            restart
        # if input is "no" switch to loop to false there by ending the forever loop
        elif starter == "no":
            restart = False


# a function that decodes a text, takes who parameters of the text and the number to shift
def encrypt(mytext, shiftnum):
    # variable to store the string
    cipher = ""
    # go through every text inputed by user
    for letter in mytext:
        # check if the letters gotten from the user are in the alphabet list
        if letter in alphabet:
            # get the position of the letter in the alphabet list
            position = alphabet.index(letter)
            # add the position gotten to the number of times the user want the letter to shifted
            new_position = (position + shiftnum) % 26  # Use modulo to handle wrapping
            # get the new position of all the input text
            new_letter = alphabet[new_position]
            # store them as string
            cipher += new_letter
        else:
            # if it is non-alphabet keep unchanged
            cipher += letter  # Keep non-alphabet characters unchanged
    # print the final encoded text
    print(f"The encoded text is: {cipher}")


# A function that decodes a text, takes two parameters
def decrypt(mytext, shiftnum):
    # variable to store the string
    cipher = ""
    # go through every string the user input
    for letter in mytext:
        # check if user input is contained in the alphabet list
        if letter in alphabet:
            # get the position of the letters the user input in the list
            position = alphabet.index(letter)
            # subtract the position with the previous number to get the decoded text
            new_position = (position - shiftnum) % 26  # Use modulo to handle wrapping
            # get the new position of input text in the list
            new_letter = alphabet[new_position]
            # store them in variable as a string
            cipher += new_letter
        else:
            cipher += letter  # Keep non-alphabet characters unchanged
    # print the decoded text
    print(f"The decoded text is: {cipher}")


# calling the main function
main()
