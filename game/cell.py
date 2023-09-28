from game.tile import Tile
class Cell:
    def __init__(self, multiplier=1, multiplier_type='', letter=None, status='active'):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.status = status
    def add_letter(self,letter:Tile):
        self.letter = letter
    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        if self.multiplier_type == 'word':
            return self.letter.value