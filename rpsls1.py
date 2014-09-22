#Defines a helper function that converts each choice into a number.
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return 'error'

#Defines a helper function that converts the numbers into a choice.    
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "error"

#Imports the package "random".    
import random

#Defining the main function. 
def rpsls(player_choice):
    print
    print "Player has chosen", player_choice,"!"
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    print "Computer has chosen " + number_to_name(comp_number)+"!"
    diff = (name_to_number(player_choice)-comp_number)%5
    if diff == 1:
        print "Player wins!"
    elif diff == 2:
        print "Player wins!"
    elif diff == 3:
        print "Computer wins!"
    elif diff == 4:
        print "Player wins!"
    elif diff == 0:
        print "Draw"
    

rpsls("paper")

    