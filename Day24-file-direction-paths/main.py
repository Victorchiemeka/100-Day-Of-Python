PLACEHOLDER = "[names]"
# Read the starting letter letter_template
with open(
    "./Input/Letters/starting_letter.txt",
    "r",
) as file:
    letter_template = file.read()

# Read the list of names
with open(
    "./Input/Names/invited_names.txt",
    "r",
) as name_file:
    names = name_file.readlines()

# Process each name and create personalized letters
for name in names:
    # Remove leading/trailing whitespace and newline characters
    name = name.strip()

    # Replace the [name] placeholder with the actual name
    personalized_letter = letter_template.replace(PLACEHOLDER, name)

    # Save the personalized letter in the "ReadyToSend" folder
    with open(
        f"/home/vitao/Desktop/100-Day-Of-Python/Day24-file-direction-paths/Output/ReadyToSend/{name}_letter.txt",
        "w",
    ) as send:
        send.write(personalized_letter)

print("Personalized letters created and saved.")
