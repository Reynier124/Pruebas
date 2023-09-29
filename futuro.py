# Changelog
def test_calculate_score(self):
        game = Scrabble(2)
        word = "Hola"
        location = (7,7)
        orientation = "H"
        self.assertEqual(game.calculate_score(word, location, orientation), 15)
        
## [0.2.0] - 2023-09-26

###  Added

- Added new method for the class "Scrabble" named "string_to_tiles". This will pass one word into a list of tiles and this will use in the future for another method
- Added tests for the new method
    
#Code
def string_to_tiles(input_string):
    bag = BagTiles()
    tiles_list = []
    for letter in input_string.upper():
        for tile in bag.tiles:
            if tile.letter == letter:
                tiles_list.append(tile)
                break  
    return tiles_list
# Test
    def test_string_to_tile_hola(self):
        list_tiles = string_to_tiles("hola")
        self.assertEqual(list_tiles[0].letter, "H")
        self.assertEqual(list_tiles[0].value, 4)
        self.assertEqual(list_tiles[1].letter, "O")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "L")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)
    def test_string_to_tile_facultad(self):
        list_tiles = string_to_tiles("facultad")
        self.assertEqual(list_tiles[0].letter, "F")
        self.assertEqual(list_tiles[0].value, 4)
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "C")
        self.assertEqual(list_tiles[2].value, 2)
        self.assertEqual(list_tiles[3].letter, "U")
        self.assertEqual(list_tiles[3].value, 1)
        self.assertEqual(list_tiles[4].letter, "L")
        self.assertEqual(list_tiles[4].value, 1)
        self.assertEqual(list_tiles[5].letter, "T")
        self.assertEqual(list_tiles[5].value, 1)
        self.assertEqual(list_tiles[6].letter, "A")
        self.assertEqual(list_tiles[6].value, 1)
        self.assertEqual(list_tiles[7].letter, "D")
        self.assertEqual(list_tiles[7].value, 2)
    def test_string_to_tile_casa(self):
        list_tiles = string_to_tiles("casa")
        self.assertEqual(list_tiles[0].letter, "C")
        self.assertEqual(list_tiles[0].value, 2)
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "S")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)

## [0.2.1] - 2023-09-27

###  Added

- Added 2 method for the class "Scrabble" named "special_to_tiles" and "converter_word_to_tiles". "converter_word_to_tiles" will converter any word into a list of tiles and now "string_to_tiles" and "especial_to_tiles" is used to factorized
- Added new tests for the new methods

### Changed

- Now the method "string_to_tiles" is used to factorized the method "converter_word_to_tiles"
- Changed the tests of the method to "string_to_tiles" for test "converter_word_to_tiles"

#Code
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

#tests
    def test_converter_word_to_tiles_simple_hola(self):
        list_tiles = converter_word_to_tiles("hola")
        self.assertEqual(list_tiles[0].letter, "H")
        self.assertEqual(list_tiles[0].value, 4)
        self.assertEqual(list_tiles[1].letter, "O")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "L")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)
    def test_converter_word_to_tiles_simple_facultad(self):
        list_tiles = converter_word_to_tiles("facultad")
        self.assertEqual(list_tiles[0].letter, "F")
        self.assertEqual(list_tiles[0].value, 4)
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "C")
        self.assertEqual(list_tiles[2].value, 2)
        self.assertEqual(list_tiles[3].letter, "U")
        self.assertEqual(list_tiles[3].value, 1)
        self.assertEqual(list_tiles[4].letter, "L")
        self.assertEqual(list_tiles[4].value, 1)
        self.assertEqual(list_tiles[5].letter, "T")
        self.assertEqual(list_tiles[5].value, 1)
        self.assertEqual(list_tiles[6].letter, "A")
        self.assertEqual(list_tiles[6].value, 1)
        self.assertEqual(list_tiles[7].letter, "D")
        self.assertEqual(list_tiles[7].value, 2)
    def test_converter_word_to_tiles_simple_casa(self):
        list_tiles = converter_word_to_tiles("casa")
        self.assertEqual(list_tiles[0].letter, "C")
        self.assertEqual(list_tiles[0].value, 2)
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "S")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)
    def test_converter_word_to_tiles_complex_CH(self):
        list_tiles = converter_word_to_tiles("chita")
        self.assertEqual(list_tiles[0].letter, "CH")
        self.assertEqual(list_tiles[0].value, 5)
        self.assertEqual(list_tiles[1].letter, "I")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "T")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)
    def test_converter_word_to_tiles_complex_RR(self):
        list_tiles = converter_word_to_tiles("perro")
        self.assertEqual(list_tiles[0].letter, "P")
        self.assertEqual(list_tiles[0].value, 2)
        self.assertEqual(list_tiles[1].letter, "E")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "RR")
        self.assertEqual(list_tiles[2].value, 8)
        self.assertEqual(list_tiles[3].letter, "O")
        self.assertEqual(list_tiles[3].value, 1)
    def test_coverter_word_to_tilescomplex_LL(self):
        list_tiles = converter_word_to_tiles("llanto")
        self.assertEqual(list_tiles[0].letter, "LL")
        self.assertEqual(list_tiles[0].value, 8)
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "N")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "T")
        self.assertEqual(list_tiles[3].value, 1)
        self.assertEqual(list_tiles[4].letter, "O")
        self.assertEqual(list_tiles[4].value, 1)

## [0.2.2] - 2023-09-30

###  Added

- Added new attribute for the class "Player" named score. This is self explanatory
- Added new method for the class "Scrabble" named "calculate_score". This will add the score you get

#Code
def calculate_score(self, word):
        score = self.board.calculate_word_value(word)
        self.current_player.score += score
#test
def test_calculate_score_simple(self):
        game = Scrabble(2)
        word = [Cell(multiplier=1, letter=Tile("C",1))]
        game.next_turn()
        self.assertEqual(game.current_player.score, 0)
        game.calculate_score(word)
        self.assertEqual(game.current_player.score, 1)
    def test_calculate_score_complex(self):
        game = Scrabble(2)
        word = [Cell(multiplier=1, letter=Tile("C",1))]
        game.next_turn()
        self.assertEqual(game.current_player.score, 0)
        game.current_player.score = 5
        game.calculate_score(word)
        self.assertEqual(game.current_player.score, 6)

## [0.2.3] - 2023-09-31

###  Added

- Added new method for the class "Board" named "put_words". This method will put letter for letter in your respective cell

#code
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
#test
    def test_put_words_horizontal(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        board.put_words(word, location, orientation)
        self.assertEqual(board.grid[5][4].letter.letter, "F")
        self.assertEqual(board.grid[5][5].letter.letter, "A")
        self.assertEqual(board.grid[5][6].letter.letter, "C")
        self.assertEqual(board.grid[5][7].letter.letter, "U")
        self.assertEqual(board.grid[5][8].letter.letter, "L")
        self.assertEqual(board.grid[5][9].letter.letter, "T")
        self.assertEqual(board.grid[5][10].letter.letter, "A")
        self.assertEqual(board.grid[5][11].letter.letter, "D")
    
    def test_put_words_vertical(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "V"
        board.put_words(word, location, orientation)
        self.assertEqual(board.grid[5][4].letter.letter, "F")
        self.assertEqual(board.grid[6][4].letter.letter, "A")
        self.assertEqual(board.grid[7][4].letter.letter, "C")
        self.assertEqual(board.grid[8][4].letter.letter, "U")
        self.assertEqual(board.grid[9][4].letter.letter, "L")
        self.assertEqual(board.grid[10][4].letter.letter, "T")
        self.assertEqual(board.grid[11][4].letter.letter, "A")
        self.assertEqual(board.grid[12][4].letter.letter, "D")



## [0.2.4] - 2023-10-1

###  Added

- Added new method for the class "Board" named "display_board". This method if self explanatory but this not have test and have too much cognitive complixity

#code
    def display_board(self, placed_word=None):
        for row_index, row in enumerate(self.grid):
            row_str = ""
            for col_index, cell in enumerate(row):
                if placed_word is not None and (col_index, row_index) in placed_word["positions"]:
                    # Marcar la casilla como desactivada
                    cell.status = 'desactive'
                    row_str += f" {cell.letter.letter} "
                else:
                    if cell.status == 'active':
                        if cell.letter is None:
                            if cell.multiplier_type == 'word':
                                if cell.multiplier == 3:
                                    row_str += f"{Fore.RED}{cell.multiplier}W{Style.RESET_ALL} "
                                elif cell.multiplier == 2:
                                    row_str += f"{Fore.LIGHTMAGENTA_EX}{cell.multiplier}W{Style.RESET_ALL} "
                            elif cell.multiplier_type == 'letter':
                                if cell.multiplier == 3:
                                    row_str += f"{Fore.BLUE}{cell.multiplier}L{Style.RESET_ALL} "
                                elif cell.multiplier == 2:
                                    row_str += f"{Fore.CYAN}{cell.multiplier}L{Style.RESET_ALL} "
                            else:
                                row_str += " - "
                        else:
                            row_str += f" {cell.letter.letter} "
                    else:
                        row_str += "###"
            print(row_str)