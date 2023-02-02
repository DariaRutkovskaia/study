with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    starting_letter = letter_file.read()

for name in names:
    name = name.strip()
    text = starting_letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as ready_letter:
        ready_letter.write(text)
