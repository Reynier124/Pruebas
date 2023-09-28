import unittest
from game.scrabble import Scrabble
from game.player import Player
from game.board import Board

class TestScrabble(unittest.TestCase):
    def test_scrabble(self):
        scrabble_1 = Scrabble(3)
        self.assertIsNotNone(scrabble_1.board, None)
        self.assertEqual(len(scrabble_1.players),3)
        self.assertEqual(scrabble_1.turn, 1)
    def test_unique_id(self):
        game_1 = Scrabble(1)
        game_2 = Scrabble(1)
        self.assertNotEqual(game_1.gameid, game_2.gameid)
    def test_next_turn_when_game_is_starting(self):
        game = Scrabble(2)
        game.next_turn()
        self.assertEqual(game.current_player, game.players[0])
    def test_next_turn_when_game_is_not_the_first(self):
        game = Scrabble(2)
        game.current_player = game.players[0]
        game.next_turn()
        self.assertEqual(game.current_player, game.players[1])
    def test_next_turn_when_game_is_last(self):
        game = Scrabble(2)
        game.current_player = game.players[1]
        game.next_turn()
        self.assertEqual(game.current_player, game.players[0])
    def test_next_turn(self):
        game = Scrabble(2)
        self.assertEqual(game.turn, 1)
        game.next_turn()
        self.assertEqual(game.turn, 2)
    def test_playing(self):
        game = Scrabble(1)
        self.assertEqual(game.playing(), True)
    
    def test_validate_word(self):
        game = Scrabble(2)
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        self.assertEqual(game.validate_word(word,location,orientation), True)
    
    def test_string_to_tile_hola(self):
        game = Scrabble(2)
        list_tiles = game.string_to_tiles("hola")
        self.assertEqual(list_tiles[0].letter, "H")
        self.assertEqual(list_tiles[0].value, 4)
        self.assertEqual(list_tiles[1].letter, "O")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "L")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)
    def test_string_to_tile_facultad(self):
        game = Scrabble(2)
        list_tiles = game.string_to_tiles("facultad")
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
        game = Scrabble(2)
        list_tiles = game.string_to_tiles("casa")
        self.assertEqual(list_tiles[0].letter, "C")
        self.assertEqual(list_tiles[0].value, 2)
        self.assertEqual(list_tiles[1].letter, "A")
        self.assertEqual(list_tiles[1].value, 1)
        self.assertEqual(list_tiles[2].letter, "S")
        self.assertEqual(list_tiles[2].value, 1)
        self.assertEqual(list_tiles[3].letter, "A")
        self.assertEqual(list_tiles[3].value, 1)
        
if __name__ == '__main__':
    unittest.main()