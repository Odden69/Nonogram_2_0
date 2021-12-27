from pathlib import Path
from library.clear_screen import clear_screen


def print_start_menu():
    """
    Prints the start message to the terminal
    """
    clear_screen()
    message = '''Welcome to the Nonogram game!\n
        Choose one of the following options by typing the number.\n
        1. How to play.\n
        2. Play Game\n'''
    print(message)
    get_player_input_start_menu()


def get_player_input_start_menu():
    """
    Gets start menu input from player
    """
    while True:
        try:
            choice = int(input('Make your choice: \n'))
        except ValueError:
            print('        That was not a number. Please try again.\n')
        else:
            if choice == 1:
                print_how_to_play_menu()
            elif choice == 2:
                break
            else:
                print('       That was not a valid choice, '
                      'please type 1 or 2\n')


def print_how_to_play_menu():
    """
    Prints info on how to play the game to the terminal
    """
    clear_screen()
    message = '''How to play the Nonogram game!\n
        Choose one of the following options by typing the number.\n
        1. Common rules of a Nonogram.\n
        2. How to play this Nonogram Game\n
        3. Go back to the main menu\n'''
    print(message)
    get_player_input_how_to_play_menu()


def get_player_input_how_to_play_menu():
    """
    Gets how to play menu input from player
    """
    while True:
        try:
            choice = int(input('Make your choice: \n'))
        except ValueError:
            print('        That was not a number. Please try again.\n')
        else:
            if choice in (1, 2):
                clear_screen()
                print_how_to_play(choice)
            elif choice == 3:
                from library.run_game import run_game
                run_game()
            else:
                print('       That was not a valid choice, '
                      'please type 1, 2 or 3\n')


def print_how_to_play(choice):
    """
    Prints how to play information from text files
    The pathlib info was found on https://stackoverflow.com/questions/...
    8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
    """
    txt_common_1 = Path('assets/how_to_play_docs/how_to_play_common_1.txt')\
        .read_text()
    txt_common_2 = Path('assets/how_to_play_docs/how_to_play_common_2.txt')\
        .read_text()
    txt_this_game_1 = Path('assets/how_to_play_docs/how_to_play_this_1.txt')\
        .read_text()
    txt_this_game_2 = Path('assets/how_to_play_docs/how_to_play_this_2.txt')\
        .read_text()
    txt_this_game_3 = Path('assets/how_to_play_docs/how_to_play_this_3.txt')\
        .read_text()
    if choice == 1:
        print(txt_common_1 + '\n')
        input('Press enter to continue: \n')
        clear_screen()
        print(txt_common_2 + '\n')
    else:
        print(txt_this_game_1 + '\n')
        input('Press enter to continue: \n')
        clear_screen()
        print(txt_this_game_2 + '\n')
        input('Press enter to continue: \n')
        clear_screen()
        print(txt_this_game_3 + '\n')
    input('Press enter to go back to how to play menu: \n')
    print_how_to_play_menu()


def get_board_size_from_player():
    """
    Gets board size input from player
    """
    while True:
        try:
            size = int(input('Choose your preferred board size. '
                             'Enter a number between 4 and 10: \n'))
        except ValueError:
            print('        That was not a number. Please try again. \n')
        else:
            if 4 <= size <= 10:
                break
            print('That was not a valid choice, please enter a number '
                  'between 4 and 10 \n')
    return size
