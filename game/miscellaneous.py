from game.bagtiles import BagTiles

class Miscellaneous:
    def string_to_tiles(self, input_string, list):
        bag = BagTiles()
        for letter in input_string.upper():
            for tile in bag.tiles:
                if tile.letter == letter:
                    list.append(tile)
                    break

    def especial_to_tiles(self, input_string, list):
        bag = BagTiles()
        for tile in bag.tiles:
            if tile.letter == input_string.upper():
                list.append(tile)
                break

    def converter_word_to_tiles(self, word):
        tiles_list = []
        i = 0
        while i < len(word):
            if i < len(word) - 1:
                two_letter_combo = word[i:i+2]
                print(two_letter_combo)
                if two_letter_combo.upper() in ('CH', 'LL', 'RR'):
                    self.especial_to_tiles(two_letter_combo, tiles_list)
                    i += 2
                else:
                    self.string_to_tiles(word[i], tiles_list)
                    i += 1
            else:
                self.string_to_tiles(word[i], tiles_list)
                i += 1
        return tiles_list
    
    def compare_tiles_and_letters(self, tile, word):
        if tile is not None:
            if tile.letter.lower() == word:
                return 1
            else:
                return 0
        else:
            return
    
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