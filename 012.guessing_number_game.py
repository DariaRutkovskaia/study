import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
hidden_number = random.randint(1, 100)


def number_game():
    game_over = False
    global attempts_remaining
    while not game_over and attempts_remaining > 0:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        print("Guess again.")
        user_guess = int(input("Make a guess: "))
        if user_guess == hidden_number:
            print(f"You got it! The answer was {hidden_number}.")
            game_over = True
        elif user_guess > hidden_number:
            attempts_remaining -= 1
            print("Too high.")
        elif user_guess < hidden_number:
            attempts_remaining -= 1
            print("Too low.")
    if attempts_remaining == 0:
        print(f"You run out of attempts, you lose. The answer was {hidden_number}")


if input("Choose a difficulty. Type 'easy' or 'hard' ").lower() == "easy":
    attempts_remaining = 10
else:
    attempts_remaining = 5
number_game()
