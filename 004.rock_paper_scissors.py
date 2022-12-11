import random

rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]
computer_num = random.randint(0, 2)
player_num = int(input("What do you choose?\n Rock - 1\n Paper - 2\n Scissors - 3\n")) - 1

computer_choice = game[computer_num]
players_choice = game[player_num]
print(f"Player's choice:\n {players_choice}")
print(f"Computer's choice:\n {computer_choice}")
if computer_num == player_num:
    print("It's a draw")
elif player_num - computer_num == 1 or player_num - computer_num == -2:
    print("Player wins!!")
else:
    print("Computer wins!")
