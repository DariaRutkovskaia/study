from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, direction_func):
    if direction_func == "decode":
        shift_amount = -shift_amount
    cipher_text = ""
    for letter in plain_text:
        if letter not in alphabet:
            new_letter = letter
        else:
            new_index = alphabet.index(letter) + shift_amount
            if new_index > len(alphabet) - 1:
                new_index -= len(alphabet)
            new_letter = alphabet[new_index]
        cipher_text += new_letter
    print(f"The {direction_func}d text is\n{cipher_text}")


should_end = False
while should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > len(alphabet):
        shift = shift % len(alphabet)
    caesar(text, shift, direction)
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if answer.lower() == 'no':
        should_end = True
        print("Kiitos! Hej-hej!!")
