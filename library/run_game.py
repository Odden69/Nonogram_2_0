import library.start_menu
from library.game_board import GameBoard
from library.clear_screen import clear_screen


def play_game(game_board):
    """
    Prints the board and gets new game input from player until the game
    is finished or the player aborts.
    """
    while True:
        clear_screen()
        game_board.print_game_board()
        game_board.player_pattern = game_board.get_board_input_from_player()


def restart_game(game_board):
    """
    Restarts the game with the same game_pattern as the game before
    """
    print('\nYou chose to replay the game to try to solve the same '
          'pattern again.\nGood luck!\n')
    input('Press Enter to continue: \n')
    game_board.player_pattern = game_board.populate_player_pattern()
    play_game(game_board)


def run_game():
    """
    Runs the application.
    """
    library.start_menu.print_start_menu()
    size = library.start_menu.get_board_size_from_player()
    game_board = GameBoard(size)
    game_board.game_pattern = game_board.populate_game_pattern()
    game_board.player_pattern = game_board.populate_player_pattern()
    play_game(game_board)


run_game()
