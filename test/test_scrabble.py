import unittest
from game.scrabble import Scrabble
from game.player import Player
from game.board import Board
from game.cell import Cell
from game.tile import Tile

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
        
if __name__ == '__main__':
    unittest.main()