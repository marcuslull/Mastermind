# This game simulates the game Mastermind. The program will generate a secret code
# and then allow the user to have multiple guesses. The program will analyze each
# player guess and give hints to help the player deduce the code.
# the purpose of this is to pass an introductory to Python course and have a little fun :)

# imports
import random

# global variables
win = False
turns = 1
secret = ()
picks = ()
board = []


# functions
def instructions():
    """Prints the mastermind instructions to the console"""
    print("\nWelcome to Mastermind!\n")
    print("Mastermind is a game of deductive reasoning where you try to guess,\nthrough a series of clues, the color "
          "and order of a set of pegs in as few guesses as possible.\n")
    print("Instructions:\n")
    print("The program will pick 4 colors, you try to guess the correct color and order.")
    print("After each pick the program will give you hints including how many colors you guessed correctly\nand if "
          "they are in the correct position.")
    print("You continue to make guesses using the hints provided until you guess all 4 colors\nin the correct order.\n")
    print("The colors to choose from are:")
    print("Red, Green, Blue, Yellow, White, Purple\n")
    print("Good Luck!\n")


def initialize():
    """Initialize the game global variables. Used at the start of each game."""
    # changing scope
    global win, turns, secret, picks, board
    # setting global variables back to defaults
    win = False
    turns = 1
    secret = ()
    picks = ()
    board = []


def pick_secret():
    """Picks 4 random colors and returns tuple"""
    colors = ("R", "G", "B", "Y", "W", "P")  # possible color selection
    secret_picks = []  # selection
    # Randomly selects a color from colors and adds it to secret
    while len(secret_picks) != 4:
        choice = colors[random.randint(0, 5)]
        if choice not in secret_picks:  # we cannot have duplicate colors
            secret_picks.append(choice)
    return tuple(secret_picks)  # cast secret as a tuple. We rely on the immutability and uniqueness of a tuple.


def guess():
    """Prompts the player for their selection and validates. Returns picks tuple"""
    colors = ("R", "G", "B", "Y", "W", "P")  # possible color selection
    potential_picks = []  # players selection
    # The player should keep getting prompted for a valid selection
    while True:
        print("\nPlease select 4 unique colors for your guess using the first letter for each color")
        print("Colors are: Red, Green, Blue, Yellow, White, and Purple")
        print("Example: RGYP (Red, Green, Yellow, Purple)\n")
        # getting the players selection and formatting into easy to work with data
        player_input = input("Your guess: ").replace(" ", "").upper()
        # loop through the players input selection
        for color in player_input:
            if color in colors:  # check for valid color
                potential_picks.append(color)  # keeping only good selections
        # casting the list as a set to remove duplicates and check for the proper length (4)
        if len(set(potential_picks)) == 4:
            return tuple(potential_picks)  # cast as a tuple and return
        print("\nYour selection was invalid\n")  # Inform the user of a bad selection
        potential_picks = []  # reset the list so we can test a new selection


def display(game_board):
    """Displays the board list in a game board format"""
    print("\n    GAME BOARD")
    for player_guess in game_board:  # loops through each inner tuple
        print(player_guess)


def compare(game_secret, player_picks):
    """
    Takes secret and picks tuples as input and compares their colors and locations.
    based on the comparison a set of hints will be displayed to the player
    If the player got all four correct it outputs a congratulatory message and ends the game.
    """
    global win, turns  # change the scope of these variables
    color_and_position = 0
    color_wrong_position = 0
    # iterate over the players picks and compare them to the secret picks
    for color in player_picks:
        if color == game_secret[player_picks.index(color)]:  # comparing color and location
            color_and_position += 1
        else:
            if color in game_secret:  # only comparing color
                color_wrong_position += 1
    if color_and_position == 4:  # this is the win condition, congratulate the player and end this game
        win = True
        print("\nCongratulations - You are the Mastermind!")
        print("You cracked the code in", turns, "turns.")
    else:  # if the player did not win then display the hints and increment the turn global variable
        print("\nHint:", color_and_position, "are the correct color and in the correct position.")
        print("Hint:", color_wrong_position, "are the correct color but wrong position.")
        turns += 1


# main program
while True:  # launch and loop the game menu until 3(quit) is selected
    print("\nMastermind - A game of deductive reasoning\n")
    print("What would you like to do?")
    print("1: view the instructions \n2: start a game \n3: quit")
    menuChoice = input("1-3?: ")  # menu item as user input
    if menuChoice == "1":  # selection 1 launch the instructions function
        instructions()
    elif menuChoice == "2":  # selection 2 launch the game
        initialize()  # reset all globals
        secret = pick_secret()  # pick a secret code
        # print(secret) # comment/uncomment to see the secret code for debugging
        # loop over the main game logic until win boolean is True
        while not win:
            picks = guess()  # get and validate the players picks
            board.append(picks)  # save the validated picks to the board
            display(board)  # display the board
            compare(secret, picks)  # compare the players guess to the secret
    else:  # handle menu choice 3 or an invalid selection
        if menuChoice == "3":
            break  # terminate the program
        print("Please make a valid selection, 1-3")  # warning message to the player
