import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
print(logo)
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
word_length = len(chosen_word)
lives = 6
display = []

for i in range(word_length):
  display.append("_")
print(' '.join(display))
while "_" in display and lives > 0:
  guess = input("Try to guess a letter:  ").lower()
  if guess in display:
    print("You have already guess this letter")
  if guess not in chosen_word:
    lives -= 1
    print(f"This letter {guess} is not in the word\n{stages[lives]}")
  else:
    for i in range(word_length):
      if chosen_word[i] == guess:
        display[i] = guess
  print(' '.join(display))
else:
  if "_" not in display:
    print("You win")
  else:
    print(f"You lose chosen word was {chosen_word}")
