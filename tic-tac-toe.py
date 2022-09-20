""" W02 Tic-Tac-Toe Game 
by Cynthia Rawlings """

def instructions():
    """ Gives the begining instructions to the players. """
    print()
    print()
    print("Welcome to Tic-Tac-Toe!")
    print()
    print("1 | 2 | 3")
    print("- + - + - ")
    print("4 | 5 | 6")
    print("- + - + - ")
    print("7 | 8 | 9")
    print()
    print("To play type in the number that corresponds with the square you want.")
    print()

def make_a_move(player, game_board):
    """ Player (X or O) and game_board as paramaters.
    Gets the current player's desired space and checks
    if it is available. If it is, it is added to the game board. """

    player_input = input(f"{player}, where would you like to move? (1-9) ")
    while player_input.isdigit() == False:
        # Check for number
        player_input = input(f"{player}, please type in a number (1-9) ")
    
    player_space = int(player_input)
    player_index = player_space - 1

    while game_board[player_index] == "X" or game_board[player_index] == "O":
        # Check to make sure that that space isn't already taken
        player_input = input(f"That space is already taken. {player}, where else would you like to move? (1-9) ")
        while player_input.isdigit() == False:
            # Check for number
            player_input = input(f"{player}, please type in a number (1-9) ")

        player_space = int(player_input)
        player_index = player_space - 1

    game_board[player_index] = player

    check_for_winner(player, game_board)
    
def check_for_winner(player, game_board):
    """ Checks to see if any player won, or if the game is tied. 
    If not, changes the player and calls the make_a_move function. """

    print_game_board(game_board)

    outcome = "Continue"

    # Check if X won
    victor = compare_places("X", game_board)

    if victor == "X":
        outcome = "X Won!"
    else:
        # Check if O won
        victor = compare_places("O", game_board)
        if victor == "O":
            outcome = "O Won!"
        else:
            # Check if there is a tie
            any_open_space = False

            for space in game_board:
                if isinstance(space, int) == True:
                    any_open_space = True

            if any_open_space == False:
                outcome = "It was a Tie, too bad."
    
    # If there is no victor and it's not a tie, continue playing
    if outcome == "Continue":
        # Swap players
        if player == "X":
            player = "O"
        else:
            player = "X"

        make_a_move(player, game_board)    
    else:
       print(outcome)
       print()

def compare_places(player, game_board):
    """ Takses player and game_board as paramaters.
    checks each winning pattern to see if the player won. """

    # Create a list of all the spaces the player owns
    player_owned = []
    index = 1

    for space in game_board:
        if space == player:
            player_owned.append(index)
            index += 1
        else:
            index += 1

    # Check the player_ownewd for winning patterns
    winning_patterns = [
        [1, 2, 3],
        [1, 5, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 5, 7],
        [3, 6, 9],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Only check if the player has more then 2 spaces
    if len(player_owned) > 2:
        # check all the winning patterns
        for pattern in winning_patterns:
            num_matches = 0
            # for each digit in each pattern
            for digit in pattern:
                # for each space that the player owns
                for owned in player_owned:
                    if digit == owned:
                        num_matches += 1
                if num_matches > 2:
                    print(f"Congrats! {player} Won!")
                    print()
                    quit()
            

def print_game_board(game_board):
    """Takes game_board as a paramater. Prints the current game_board to the screen. """
    print()
    print(f"{game_board[0]} | {game_board[1]} | {game_board[2]}")
    print("- + - + - ")
    print(f"{game_board[3]} | {game_board[4]} | {game_board[5]}")
    print("- + - + - ")
    print(f"{game_board[6]} | {game_board[7]} | {game_board[8]}")
    print()

def main():
    """ The main function that orders the game. """
    game_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    instructions()
    player = "X"
    make_a_move(player, game_board)
    
main()
