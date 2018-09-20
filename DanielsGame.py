# Ask for player name
# pr = player_response
pr2 = str
pr3 = str
pr4 = str
pr5 = str
pr6 = str
pr7 = str
pr8 = str


print("""Welcome to my game, please use all lower case letters in every answer, except when it asks you for a name..
Please do not leave any answers blank.""")

player_name = input("Whats your name?  ")

print("Hello", player_name)

player_response = input("Would you like to play this game with me?  ")
if player_response == "yes":
    print("Awesome!")
    pr2 = input("Now lets begin, you start at fork in the road which way do you pick {}? Left or Right?  ".format(player_name))
else:
    print("Ah well, that sucks....")
    
if pr2 == "right":
    print("While walking down the right path you encounter an Old Woman.")
    pr3 = input("Do you 'talk' to her or 'pass' her by?  ")
    if pr3 == "talk":
        print("""\nOLd Woman: Ah I've been waiting for you.
{}: Me?
Old Woman: Yes Im here to warn you about a group of bandits on the road up ahead.
Old Woman: I would suggest taking this path behind me that goes through the forest.""".format(player_name))
        pr5 = input("""\nDo you take the Old Woman's advise and take path or do you not listen to her?
Pick 'take path' or 'dont listen'.  """)
        if pr5 == "take path":
            pass
        elif pr5 == "dont listen":
            pass
        
    elif pr3 == "pass":
        print("As you walk by her, you feel her gaze come to rest on you, so you hurry past her.")
        print("""\nAs your walking down the path, you face-to-face with two bandits.
\nBandit1: Hey, give us all your money and you may live.
{}: I-I don't have any money.
Bandit2: Oh, you don't do ya?
Bandit1: Haha, then this will be fun.""".format(player_name))
        pr6 = input("""\nYou see a village down the path. \nDo you 'run' past the bandits or 'fight' them?  """)
        if pr6 == "run":
            pass
        elif pr6 == "fight":
            pass

elif pr2 == "left":
    print("At the end of the left path you find a Berserker who wants to join you on your journey.")
    pr4 = input("Do you say 'yes' to him or say 'no'?  ")
    if pr4 == "yes":
        print("Berserker: Hah, I'm glad you said yes, now lets get to that town up head.")
    elif pr4 == "no":
        print("Hahaha, well since I can't join I guess my only option is to kill you. Are you ready for a fight?")
else:
    pass 
