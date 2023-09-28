from game.cell import Cell

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

    def is_active_and_letter_multiplier(self,cell):
        return cell.status == 'active' and cell.multiplier_type == 'letter'

    def is_active_and_word_multiplier(self,cell):
        return cell.status == 'active' and cell.multiplier_type == 'word'
    
    def is_desactive_or_none_multiplier(self,cell):
        return cell.status == 'desactive' or cell.multiplier_type == ''


    def calculate_word_value(self,word):
        total_value = 0
        word_multiplier = 1

        for cell in word:
            if self.is_desactive_or_none_multiplier(cell):
                total_value += cell.letter.value
            elif self.is_active_and_letter_multiplier(cell):
                total_value += cell.calculate_value()
            elif self.is_active_and_word_multiplier(cell):
                total_value += cell.calculate_value()
                word_multiplier *= cell.multiplier
        total_value *= word_multiplier

        return total_value
    
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

    def compare_tiles_and_letters(self, tile, word):
        if tile is not None:
            if tile.letter.lower() == word:
                return 1
            else:
                return 0
        else:
            return

    def check_right_letters(self, tile, letter, list):
        if self.compare_tiles_and_letters(tile, letter) == 0:
            list[0] = 0
        elif self.compare_tiles_and_letters(tile, letter) == 1:
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