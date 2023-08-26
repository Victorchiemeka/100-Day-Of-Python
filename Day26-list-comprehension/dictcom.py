sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# Split the sentence into a list of words
covert_to_list = sentence.split()


# Define the function to calculate the length of a list
def calculate_length(my_list):
    return len(my_list)


# Create a dictionary with words as keys and their lengths as values
result = {word: calculate_length(word) for word in covert_to_list}
print(result)
