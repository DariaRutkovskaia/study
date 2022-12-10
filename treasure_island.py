print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


frst_question = input("You are standing on crossroad. Where do you want to turn? Left or right? L or R")
if frst_question.lower() == "l":
  scnd_question = input("Ok! You see a big clear lake in front of you. What you gonna do: swim across it or wait for the night? S or W ")
  if scnd_question.lower() == "w":
    trd_quetion = input("Suddenly you see little house in the forest from the left side. It has 3 doors yellow blue and red. Which one you want to open? Y, B or R?")
    if trd_quetion.lower() == "y":
      print(" You win!! Good job!!<3")
    elif trd_quetion.lower() == "b":
       print("You have been eaten by beast. Game over!!!")
    elif trd_quetion.lower() == "r":
       print("You have been burned by fire. Game over!!!")
    else:
       print("Game over")

  else:
    print("You have been attacked by trout. Game over!!!")

else:
  print("Sorry, you're killed by crazy old lady. Game over! ")
