import unittest
from game.player import Player
from game.tile import Tile
from game.bagtiles import BagTiles

class TestPlayer(unittest.TestCase):
    def test_player(self):
        player1 = Player()
        self.assertEqual(player1.rack,[])
    
    def test_player_get_tile(self):
        bag1 = BagTiles()
        player = Player()
        player.get_tiles(3,bag1)
        self.assertEqual(len(player.rack),3)

    def test_player_exchange(self):
        bag1 = BagTiles()
        player = Player()
        player.rack = [Tile('A', 1), Tile('B',3), Tile('C',2)]
        player.exchange_tiles(2,bag1)
        self.assertEqual(len(player.rack),3)
        self.assertEqual(len(bag1.tiles),29)
    
    def test_validate_rack_true(self):
        player_1 = Player()
        tiles = [Tile("H",1),Tile("O",1),Tile("L",1),Tile("A",1)]
        player_1.rack = [Tile("H",1),Tile("O",1),Tile("L",1),Tile("A",1), Tile("Z",1), Tile("Z",1), Tile("Z",1)]
        is_valid = player_1.has_letters(tiles)
        assert is_valid == True
    
    def test_validate_rack_false(self):
        player_1 = Player()
        tiles = [Tile("H",1),Tile("O",1),Tile("L",1),Tile("A",1)]
        player_1.rack = [Tile("H",1),Tile("O",1),Tile("E",1),Tile("A",1), Tile("Z",1), Tile("Z",1), Tile("Z",1)]
        is_valid = player_1.has_letters(tiles)
        assert is_valid == False