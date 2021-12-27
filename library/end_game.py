"""
Contains functions to give the player options at the end of the game
"""
from library.clear_screen import clear_screen


def quit_game(game_board):
    """
    Prints an options message at the end of a game
    """
    clear_screen()
    message = '''Thank you for playing the Nonogram game!\n
        Choose one the following options by typing the number.\n
        1. Back to the start menu.\n
        2. Play the same game again. \n'''
    print(message)
    get_players_input_end_menu(game_board)


def get_players_input_end_menu(game_board):
    """
    Gets the players choice after finishing a game
    """
    while True:
        try:
            choice = int(input('Make your choice: \n'))
        except ValueError:
            print('        That was not a number. Please try again.\n')
        else:
            if choice == 1:
                from library.run_game import run_game
                run_game()
            elif choice == 2:
                from library.run_game import restart_game
                restart_game(game_board)
            else:
                print('       That was not a valid choice, '
                      'please type 1 or 2.\n')
