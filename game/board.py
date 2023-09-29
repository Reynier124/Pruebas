from game.cell import Cell
from game.miscellaneous import Miscellaneous
from colorama import Fore, Style

class Board:
    def __init__(self):
        board_multipliers = [
            ["3W", None, None, "2L", None, None, None, "3W", None, None, None, "2L", None, None, "3W"],
            [None, "2W", None, None, None, "3L", None, None, None, "3L", None, None, None, "2W", None],  
            [None, None, "2W", None, None, None, "2L", None, "2L", None, None, None, "2W", None, None], 
            ["2L", None, None, "2W", None, None, None, "2L", None, None, None, "2W", None, None, "2L"],  
            [None, None, None, None, "2W", None, None, None, None, None, "2W", None, None, None, None],  
            [None, "3L", None, None, None, "3L", None, None, None, "3L", None, None, None, "3L", None],  
            [None, None, "2L", None, None, None, "2L", None, "2L", None, None, None, "2L", None, None],  
            ["3W", None, None, "2L", None, None, None, "2W", None, None, None, "2L", None, None, "3W"],  
            [None, None, "2L", None, None, None, "2L", None, "2L", None, None, None, "2L", None, None],  
            [None, "3L", None, None, None, "3L", None, None, None, "3L", None, None, None, "3L", None],  
            [None, None, None, None, "2W", None, None, None, None, None, "2W", None, None, None, None],  
            ["2L", None, None, "2W", None, None, None, "2L", None, None, None, "2W", None, None, "2L"],  
            [None, None, "2W", None, None, None, "2L", None, "2L", None, None, None, "2W", None, None],  
            [None, "2W", None, None, None, "3L", None, None, None, "3L", None, None, None, "2W", None],  
            ["3W", None, None, "2L", None, None, None, "3W", None, None, None, "2L", None, None, "3W"] 
        ]
        self.grid = [
            [self.put_multipliers(multiplier) for multiplier in row]
            for row in board_multipliers
        ]

    def put_multipliers(self, multiplier):
        if multiplier is None:
            return Cell()
        multiplier_type = multiplier[-1]
        multiplier_value = int(multiplier[0])
        if multiplier_type == "W":
            return Cell(multiplier=multiplier_value, multiplier_type="word")
        elif multiplier_type == "L":
            return Cell(multiplier=multiplier_value, multiplier_type="letter")
    
    def put_words(self, word, location, orientation):
        misc = Miscellaneous()
        list_word = misc.converter_word_to_tiles(word)
        column = location[0]
        row = location[1]
        i = 0
        for _ in list_word:
            self.grid[column][row].letter = list_word[i]
            if orientation == "H":
                row += 1
                i += 1
            elif orientation == "V":
                column += 1
                i += 1

    def validate_word_inside_board(self,word, location, orientation):
        column = location[0]
        row = location[1]
        word_length = len(word)
        if orientation == "H":
            return row + word_length <= 15
        elif orientation == "V":
            return column + word_length <= 15
    
    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        else:
            return False
        
    def word_in_the_center(self, word, location, orientation):
        coordinate = {"H":location[0], "V" : location[1]}
        central_coordinate = coordinate.get(orientation)
        if central_coordinate == 7:
            return self.validate_word_inside_board(word, location, orientation)
        else:
            return False

    def check_right_letters(self, tile, letter, list):
        misc = Miscellaneous()
        if misc.compare_tiles_and_letters(tile, letter) == 0:
            list[0] = 0
        elif misc.compare_tiles_and_letters(tile, letter) == 1:
            if list[0] == -1:
                list[0] = 1
            list.append(1)
    
    def check_conditions(self, list, word, location, orientation):
        return list[0] > 0 and self.validate_word_inside_board(word, location, orientation) is True

    def validate_word_horizontal(self, word, location, orientation):
        column = location[0]
        row = location[1]
        found_letter = [-1]
        for i in range(len(word)):
            actual_tile = self.grid[column][row + i].letter
            self.check_right_letters(actual_tile, word[i], found_letter)
        return self.check_conditions(found_letter, word, location, orientation)
    
    def validate_word_vertical(self, word, location, orientation):
        column = location[0]
        row = location[1]
        found_letter = [-1]
        for i in range(len(word)):
            actual_tile = self.grid[column + i][row].letter
            self.check_right_letters(actual_tile, word[i], found_letter)
        return self.check_conditions(found_letter, word, location, orientation)
    
    def validate_word_place_board(self, word, location, orientation):
        if self.is_empty() is True:
           return self.word_in_the_center(word, location, orientation)
        else:
            if orientation == "H":
                return self.validate_word_horizontal(word, location, orientation)
            else:
                return self.validate_word_vertical(word, location, orientation)
    
    def display_board(self, placed_word=None):
        for row_index, row in enumerate(self.grid):
            row_str = ""
            for col_index, cell in enumerate(row):
                if placed_word is not None and (col_index, row_index) in placed_word["positions"]:
                    row_str += f" {cell.letter.letter} "
                    self.deactivate_cell(cell) 
                else:
                    if cell.status == 'active':
                        row_str += self.format_cell_contents(cell)
                    else:
                        row_str += "###"
            print(row_str)

    def format_cell_contents(self, cell):
        if cell.letter is None:
            if cell.multiplier_type == 'word':
                return self.format_word_multiplier(cell.multiplier)
            elif cell.multiplier_type == 'letter':
                return self.format_letter_multiplier(cell.multiplier)
            else:
                return " - "
        else:
            return f" {cell.letter.letter} "

    def format_word_multiplier(self, multiplier):
        if multiplier == 3:
            return f"{Fore.RED}{multiplier}W{Style.RESET_ALL} "
        elif multiplier == 2:
            return f"{Fore.LIGHTMAGENTA_EX}{multiplier}W{Style.RESET_ALL} "
        else:
            return f"{multiplier}W "

    def format_letter_multiplier(self, multiplier):
        if multiplier == 3:
            return f"{Fore.BLUE}{multiplier}L{Style.RESET_ALL} "
        elif multiplier == 2:
            return f"{Fore.CYAN}{multiplier}L{Style.RESET_ALL} "
        else:
            return f"{multiplier}L "

    def deactivate_cell(self, cell):
        cell.status = 'desactive'
