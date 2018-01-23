#1)Select a random choice from the three items: rock, paper, or scissors. Save this choice in a variable named choice.
# 2)Ask the player for their choice. Use an integer value, where 1 = rock, 2 = paper, and 3 = scissors.
# 3)Read the player’s selection into a variable named player.
# 4)If player is equal to choice:
# 5)  Print the message “Tie. We’ll try again.”
# 6)  Repeat from step 1.
# 7)If player is equal to rock:
# 8) If choice is equal to scissors go to step 17
# 9) Else go to step 18.
# 10)If player is equal to paper:
# 11)  If choice is equal to scissors go to step 17
# 12)Else go to step 18.
# 13)  If player is equal to scissors:
# 14)If choice is equal to rock go to step 17
# 15)  Else go to step 18.
# 16)Print error message and terminate.
# 17)Print “computer wins” and terminate.
# 18)Print “You win” and terminate.

import random


comp_choice = random.randint(1,3)
print("Hello welcome to RPS game")
username = input("What is your name? ")
user_score = 0
comp_score = 0



def check_result_for_user(user):
    if user == 1:
        print("{} chose Rock 👊".format(username))
        return 1
    elif user == 2:
        print("{} chose Paper 👋".format(username))
        return 2
    elif user == 3:
        print("{} chose Scissor 🤘".format(username))
        return 3
    else:
        print("Invalid number please choose again")

def check_result_for_comp():
    if comp_choice == 1:
        print("{} chose Rock 👊".format("Computer"))
        return 1
    elif comp_choice == 2:
        print("{} chose Paper 👋".format("Computer"))
        return 2
    else:
        print("{} chose Scissor 🤘".format("Computer"))
        return 3

def print_less(user, username):
    if user == 1:
        print("{} chose Rock 👊".format(username))
        return 1
    elif user == 2:
        print("{} chose Paper 👋".format(username))
        return 2
    elif user == 3:
        print("{} chose Scissor 🤘".format(username))
        return 3
    else:
        print("Invalid number please choose again")

def game_result(num):
    global comp_score
    global user_score
    if compresult == num:
        print("{} won the game".format("Comp"))
        comp_score += 1
    else:
        print("{} won the game".format(username))
        user_score += 1


def printScore():
    print("Current Score: {} {}, Comp {}".format(username, user_score, comp_score))


while True:
    printScore()
    print(""" 
          Choose one of the options: 
          1 for Rock 👊
          2 for Paper 👋
          3 for Scissor 🤘
          😊
          """.replace("  ", ""))
    user_choice = int(input(": -> "))

    compresult = check_result_for_comp()
    userresult = check_result_for_user(user_choice)


    if compresult == userresult:
        print("Game Tied")
    elif userresult == 1:
        game_result(2)
    elif userresult == 2:
        game_result(3)
    elif userresult == 2:
        game_result(1)
    elif userresult == 3:
        game_result(1)
    printScore()

    again = input("Wanna try again?: ")

    if again == "no":
        break