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

## [0.2.0] - 2023-09-27

###  Added

- Added 2 method for the class "Scrabble" named "special_to_tiles" and "converter_word_to_tiles". "converter_word_to_tiles" will converter any word into a list of tiles and now "string_to_tiles" and "especial_to_tiles" is used to factorized
- Added new tests for the new methods

### Changed

- Now the method "string_to_tiles" is used to factorized the method "converter_word_to_tiles"
- Changed the tests of the method to "string_to_tiles" for test "converter_word_to_tiles"

#Code
def string_to_tiles(input_string, list):
    bag = BagTiles()
    for letter in input_string.upper():
        for tile in bag.tiles:
            if tile.letter == letter:
                list.append(tile)
                break
def especial_to_tiles(input_string, list):
    bag = BagTiles()
    for tile in bag.tiles:
        if tile.letter == input_string.upper():
            list.append(tile)
            break

def converter_word_to_tiles(word):
    tiles_list = []
    i = 0
    while i < len(word):
        if i < len(word) - 1:
            two_letter_combo = word[i:i+2]
            print(two_letter_combo)
            if two_letter_combo.upper() in ('CH', 'LL', 'RR'):
                especial_to_tiles(two_letter_combo, tiles_list)
                i += 2
            else:
                string_to_tiles(word[i], tiles_list)
                i += 1
        else:
            string_to_tiles(word[i], tiles_list)
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
