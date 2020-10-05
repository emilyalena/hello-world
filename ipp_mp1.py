import random

def name_to_number(name):
    """ (str) -> int

    Return the integer equivalent of the given name.

    >>> name_to_number("rock")
    0
    >>> name_to_number("scissors")
    4
    """
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        return "Error: Not a valid name"

    return number

def number_to_name(number):
    """ (int) -> str

    Return the name equivalent of the given number.

    >>> number_to_name(0)
    rock
    >>> number_to_name(3)
    lizard
    """
    
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        return "Error: Not a valid number"

    return name

def rpsls(player_choice):
    """(str) -> NoneType

    Return the winner of the game - player, computer, or a tie.

    """

    print("")
    print("Player has chosen " + player_choice + ".")
    
    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print("Computer has chosen " + comp_choice + ".")
    
    if (comp_number - player_number) < 0 or (comp_number - player_number) > 2:
        print('Player wins!')
    elif (comp_number - player_number) > 0 and (comp_number - player_number) <= 2:
        print('Computer wins!')
    else:
        print("Play again! It's a Tie.")
    


