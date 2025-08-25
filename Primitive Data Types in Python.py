#Day 3: Control Flow

print("Welcome to Treasure Island.")
print("Your objective is to naviagate through the island to find the treasure.")

#First decision
choice1 = input("""You're at a crossroad. Where do you want to go? 
            Type "left" or "right"\n""").lower()


#The user's first decision is held in the variable: choice1.
#If they chose "left", they are prompted with a second decision.
#If they chose "right" or anything else, they lose the game.
if choice1 == "left":
    choice2 = input("""You've come to a lake. There is an island in the middle of the lake.
            Type "wait" to wait for a boat. Type "swim" to swim across.\n""").lower()
    if choice2 == "wait":
        choice3 = input("""You arrive at the island unharmed. There is a house with 3 doors.
                A red door, a blue door and a yellow door. Which colour do you choose?\n""").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")