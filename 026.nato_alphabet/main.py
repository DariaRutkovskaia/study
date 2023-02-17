import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter: row.code for (index, row) in data.iterrows()}
while True:
    users_word = input("Please, enter your word: ").upper()
    try:
        code_list = [f"{letter} for {code_dict[letter]}" for letter in users_word if letter != " "]
    except KeyError:
        print("Only letters in the alphabet, please")
    else:
        print(code_list)
        break
