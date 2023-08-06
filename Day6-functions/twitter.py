def main():
    # get users input
    message = input("Input: ")
    # remove all vowels
    message_without_vowels = shorten(message)
    # print output
    print("Output: " + message_without_vowels)


def shorten(word):
    word_without_vowels = ""
    # loop through every letter
    for letter in word:
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            word_without_vowels += letter
    return word_without_vowels


if __name__ == "__main__":
    main()
