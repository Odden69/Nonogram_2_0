import random
from math import ceil
from library.clear_screen import clear_screen
from library.compare import compare_patterns


class GameBoard:
    available_rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def __init__(self, size):
        game_pattern = []
        player_pattern = []
        self.size = size
        self.game_pattern = game_pattern
        self.player_pattern = player_pattern

    def populate_game_pattern(self):
        """
        populates the game board matrix with random 0s and 1s.
        0 for empty and 1 for a filled index.
        """
        self.game_pattern = [[str(random.randint(0, 1)) for i in
                             range(self.size)] for j in range(self.size)]
        return self.game_pattern

    def populate_player_pattern(self):
        """
        populates the players board matrix with a single dot for each index.
        """
        self.player_pattern = []
        self.player_pattern = [[chr(183) for i in range(self.size)] for j in
                               range(self.size)]
        return self.player_pattern

    def get_board_element(self, i, k, direction):
        """
        Support function for calc_header function.
        Determines the order of iteration through the board list,
        depending on header direction.
        """
        if direction == 'vertical':
            return self.game_pattern[-i][k]
        return self.game_pattern[k][-i]

    def calc_header(self, direction):
        """
        Counts successive 1s in the game patten to calculate the board headers.
        """
        header = [[0 for i in range(ceil(self.size/2))] for j in
                  range(self.size)]
        # k steps through the rows/columns in the header and gets the
        # corresponding row/column in the game pattern
        # i index to step through each board coordinate for every row/column
        # j increases when the succession of 1s breaks
        k = 0
        i = 1
        j = 1
        while k < self.size:
            cont = False
            while i <= self.size:
                if self.get_board_element(i, k, direction) == '1':
                    cont = True
                    header[k][-j] += 1
                    i += 1
                elif cont:
                    # if value is 0 and cont is True, start new header inst
                    j += 1
                    i += 1
                    cont = False
                else:       # if value is 0 and cont is False, go to next coord
                    i += 1
            k += 1
            i = 1
            j = 1
        return header

    def calc_margin(self):
        """
        Returns a string of spaces depending on board size.
        Gives the space to the right of the vertical header.
        """
        margin_string = ' ' * (self.size + 1) + ((self.size % 2) * ' ')
        return margin_string

    @staticmethod
    def convert_header_integer_to_string(integer):
        """
        Converts the elements in the header list to a string depending
        on the value.
        """
        if integer == 0:
            string = ' '
        else:
            string = str(integer)
        return string

    def return_vert_header_string(self):
        """
        Converts the vertical header list to a string
        """
        string = ''
        i = 0
        while i < len(self.calc_header('vertical')[0]):
            string = string + self.calc_margin()
            for header_list in self.calc_header('vertical'):
                string_part = self.convert_header_integer_to_string(
                    header_list[i])
                string = string + string_part + ' '
            string = string + '\n'
            i += 1
        string = string[0:-2]
        return string

    def return_horiz_header_row(self, i):
        """
        Converts a list of the horizontal header list to a string
        """
        string = ' '
        for header in self.calc_header('horizontal')[i]:
            string_part = self.convert_header_integer_to_string(header)
            string = string + string_part + ' '
        return string

    def return_board_row_from_players_pattern(self, i):
        """
        Gives a string of the players pattern for each row of the board
        """
        string = ''
        k = 0
        while k < self.size:
            string_part = self.player_pattern[i][k]
            string = string + string_part + ' '
            k += 1
        return string

    def print_game_board(self):
        """
        Prints the game board
        """
        print('You can always type "Q" to quit the game, "R" to restart or \n'
              '"X" when you consider the game to be finished.\n')
        print(self.return_vert_header_string())
        i = 0
        j = 1
        string = ''
        while i < self.size:
            print(self.return_horiz_header_row(i) +
                  self.return_board_row_from_players_pattern(i) +
                  self.available_rows[i])
            i += 1
        while j <= self.size:
            string = string + str(j) + ' '
            j += 1
        print(self.calc_margin() + string + '\n')

    def get_valid_coordinates(self):
        """
        Calculates the valid coordinates depending on screen size
        """
        valid_coordinates = []
        i = 0
        j = 0
        while j < self.size:
            while i < self.size:
                valid_coordinate = f'{self.available_rows[j]}{i+1}'
                valid_coordinates.append(valid_coordinate)
                i += 1
            j += 1
            i = 0
        return valid_coordinates

    def update_player_pattern(self, new_coord, new_symbol):
        """
        Uses the players input strings and updates the player pattern
        accordingly.
        Checks if the game board is full, and in that case ends the game.
        """
        row = self.available_rows.index(new_coord[0])
        column = int(new_coord[1])-1
        self.player_pattern[row][column] = new_symbol
        check_list = [chr(183) in list for list in self.player_pattern]
        if any(check_list):
            return self.player_pattern
        clear_screen()
        self.print_game_board()
        print('You have filled the board, the game is finished\n')
        compare_patterns(self)
        return

    def get_board_input_from_player(self):
        """
        Gets the players game input
        """
        while True:
            try:
                first_entry = input('Enter the coordinate of your choice '
                                    '(e.g. A2): \n')
                new_coord = first_entry.upper()
                if new_coord == 'Q':
                    from library.run_game import run_game
                    run_game()
                    return
                if new_coord == 'R':
                    from library.run_game import restart_game
                    restart_game(self)
                    return
                if new_coord == 'X':
                    compare_patterns(self)
                elif len(new_coord) != 2:
                    raise Exception
                elif not new_coord[0].isalpha() or not new_coord[1].isdigit():
                    raise Exception
            except Exception:
                print(f'"{first_entry}" is not a valid entry. \n'
                      'Enter the coordinate in the form of one letter and one '
                      'number (e.g. A2).\n')
            else:
                try:
                    if new_coord not in self.get_valid_coordinates():
                        raise Exception
                except Exception:
                    print('The coordinate you entered is outside the board. \n'
                          'Please try again.\n')
                else:
                    break
        while True:
            try:
                second_entry = input('Do you want the coordinate to be empty '
                                     'or filled? \n'
                                     'Enter an E for empty or an F for filled:'
                                     ' \n')
                new_symbol = second_entry.upper()
                if new_symbol == 'Q':
                    from library.run_game import run_game
                    run_game()
                elif new_symbol == 'R':
                    from library.run_game import restart_game
                    restart_game(self)
                elif new_symbol == 'X':
                    compare_patterns(self)
                elif not new_symbol == 'E' and not new_symbol == 'F':
                    raise Exception
            except Exception:
                print(f'"{second_entry}" is not a valid entry. '
                      'Please try again.\n')
            else:
                break
        if new_symbol == 'E':
            new_symbol = chr(0x25A1)
        else:
            new_symbol = chr(0x25A0)
        self.update_player_pattern(new_coord, new_symbol)
        return self.player_pattern
