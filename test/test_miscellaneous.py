import unittest
from game.cell import Cell
from game.tile import Tile
from game.miscellaneous import Miscellaneous

class TestMiscellaneous(unittest.TestCase):
    def test_converter_word_to_tiles_simple_hola(self):
        misc = Miscellaneous()
        list_tiles = misc.converter_word_to_tiles("hola")
        self.assertEqual(list_tiles[0].letter, "H")
        self.assertEqual(list_tiles[0].value, 4)
        self.assertEqual(list_tiles[1].letter, "O")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "L")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)
    def test_converter_word_to_tiles_simple_facultad(self):
        misc = Miscellaneous()
        list_tiles = misc.converter_word_to_tiles("facultad")
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
        misc = Miscellaneous()
        list_tiles = misc.converter_word_to_tiles("casa")
        self.assertEqual(list_tiles[0].letter, "C")
        self.assertEqual(list_tiles[0].value, 2)
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "S")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)
    def test_converter_word_to_tiles_complex_CH(self):
        misc = Miscellaneous()
        list_tiles = misc.converter_word_to_tiles("chita")
        self.assertEqual(list_tiles[0].letter, "CH")
        self.assertEqual(list_tiles[0].value, 5)
        self.assertEqual(list_tiles[1].letter, "I")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "T")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)
    def test_converter_word_to_tiles_complex_RR(self):
        misc = Miscellaneous()
        list_tiles = misc.converter_word_to_tiles("perro")
        self.assertEqual(list_tiles[0].letter, "P")
        self.assertEqual(list_tiles[0].value, 2)
        self.assertEqual(list_tiles[1].letter, "E")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "RR")
        self.assertEqual(list_tiles[2].value, 8)
        self.assertEqual(list_tiles[3].letter, "O")
        self.assertEqual(list_tiles[3].value, 1)
    def test_coverter_word_to_tiles_complex_LL(self):
        misc = Miscellaneous()
        list_tiles = misc.converter_word_to_tiles("llanto")
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
    
    def test_compare_tile_and_letters_true(self):
        misc = Miscellaneous()
        tile = Tile("C",1)
        letter = "c"
        self.assertEqual(misc.compare_tiles_and_letters(tile, letter), 1)
    
    def test_compare_tile_and_letters_false(self):
        misc = Miscellaneous()
        tile = Tile("C",1)
        letter = "a"
        self.assertEqual(misc.compare_tiles_and_letters(tile, letter), 0)
    
    def test_simple(self):
        misc = Miscellaneous()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2)),
            Cell(letter=Tile('A',1))
        ]
        value = misc.calculate_word_value(word)
        self.assertEqual(value,5)

    def test_with_letter_multiplayer(self):
        misc = Miscellaneous()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='letter'),
            Cell(letter=Tile('A',1))
        ]
        value = misc.calculate_word_value(word)
        self.assertEqual(value,7)
    def test_with_word_multiplayer(self):
        misc = Miscellaneous()
        word = [
            Cell(letter=Tile('C',1)),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A',1))
        ]
        value = misc.calculate_word_value(word)
        self.assertEqual(value,10)
    def test_with_word_and_letter_multiplayer(self):
        misc = Miscellaneous()
        word = [
            Cell(letter=Tile('C',1), multiplier=3, multiplier_type='letter'),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word'),
            Cell(letter=Tile('A',1))
        ]
        value = misc.calculate_word_value(word)
        self.assertEqual(value,14)
    def test_with_word_and_letter_multiplayer_no_active(self):
        misc = Miscellaneous()
        word = [
            Cell(letter=Tile('C',1), multiplier=3, multiplier_type='letter', status='desactive'),
            Cell(letter=Tile('A',1)),
            Cell(letter=Tile('S',2), multiplier=2, multiplier_type='word', status='desactive'),
            Cell(letter=Tile('A',1))
        ]
        value = misc.calculate_word_value(word)
        self.assertEqual(value,5)