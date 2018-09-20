# Ask for player name
# pr = player_response
pr2 = str
pr3 = str
pr4 = str
pr5 = str
wrongAnswer = print("Your journey will be short and death is certain without any help.")

print("""Welcome to my game, please use all lower case letters in every answer, except when it asks you for a name..
Please do not leave any answers blank.""")
player_name = input("Whats your name?  ")
print("Hello", player_name)
player_response = input("Would you like to play a game with me?  ")
if player_response == "yes":
    print("Awesome!")
    pr2 = input("Now lets begin, you start at fork in the road which way do you pick {}? Left or Right?  ".format(player_name))
else:
    print("Ah well, that sucks....")


if pr2 == "right":
    print("While walking down the right path you encounter an Old Woman.")
    pr3 = input("Do you talk to her or pass her by?  ")
    if pr3 == "talk":
        pass
    elif pr3 == "pass":
        print("Your journey will be short and death is certain without any help.")
        pass
elif pr2 == "left":
    print("At the end of the left path you find a Berserker who wants to join you on your journey")
    pr4 = input("Do you say yes to him or say no?  ")
    if pr4 == "yes":
        pass
    elif pr4 == "no":
        print("Your journey will be short and death is certain without any help.")
        pass
    else:
        wrongAnswer
        pass
