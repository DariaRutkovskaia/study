import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter: row.code for (index, row) in data.iterrows()}
users_word = input("Please, enter your word: ").upper()
code_list = [f"{letter} for {code_dict[letter]}" for letter in users_word if letter != " "]
print(code_list)