"""
Contains functions to evaluate the game result and display it to the player
"""


def compare_patterns(game_board):
    """
    Compares the player and game patterns to calculate the number of errors
    """
    compare_player_pattern = game_board.player_pattern
    i = 0
    while i < game_board.size:
        list_1 = list(map(lambda item: item.replace(chr(183), '0'),
                          compare_player_pattern[i]))
        list_2 = list(map(lambda item: item.replace(chr(0x25A1), '0'), list_1))
        compare_player_pattern[i] = list(map(lambda item:
                                         item.replace(chr(0x25A0), '1'),
                                         list_2))
        i += 1
    j = 0
    k = 0
    errors = 0
    while j < game_board.size:
        while k < game_board.size:
            if game_board.player_pattern[j][k] != \
               game_board.game_pattern[j][k]:
                errors += 1
            k += 1
        j += 1
        k = 0
    result_message(errors, game_board)


def result_message(errors, game_board):
    """
    Displays the result of the game to the player
    """
    if errors > 0:
        message = f'Good job!\n\
You finished the game with {errors} error(s).\n'
    else:
        message = 'Congratulations! You finished the game ' \
                  'without any errors!\n'
    print(message)
    input('Press Enter to continue: \n')
    from library.end_game import quit_game
    quit_game(game_board)
