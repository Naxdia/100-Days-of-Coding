#Day 4: Randomisation and Python Lists
#Rock, Paper, Scissors will have 4 outcomes: Paper vs Scissors (Scissors wins), Paper vs Rock (Paper wins), Rock vs Scissors (Rock wins) and a draw if both players choose the same item. 
#However, in terms of the player, there are only 3 results: Win, Lose or Draw.

import random
#First, we need to get the user's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice == 0:
    choice_name = "Rock"
    print("You chose Rock")
elif user_choice == 1:
    choice_name = "Paper"
    print("You chose Paper")
elif user_choice == 2:
    choice_name = "Scissors"
    print("You chose Scissors")
else:
    print("You did not type a valid number, please try again.")

#The computer's choice will be randomly generated using the random module. Because the computer is limited to 3 choices, we can use else instead of elif for the last option.
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    computer_choice_name = "Rock"
    print("Computer chose Rock")
elif computer_choice == 1:
    computer_choice_name = "Paper"
    print("Computer chose Paper")
else:
    computer_choice_name = "Scissors"
    print("Computer chose Scissors")


if choice_name == computer_choice_name:
    print("It's a draw")    
#This line of code reprensents all the winning conditions for the user.
elif (choice_name == "Rock" and computer_choice_name == "Scissors") or (choice_name == "Paper" and computer_choice_name == "Rock") or (choice_name == "Scissors" and computer_choice_name == "Paper"):
    print("You win!")
else:
    print("You lose")