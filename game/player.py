import unittest
import random
from game.bagtiles import BagTiles

class Player:
    def __init__(self):
        self.rack = []
        self.score = 0

    def get_tiles(self,amount,bag=BagTiles):
        for _ in range(amount):
            self.rack.append(bag.take(1))

    def exchange_tiles(self,index,bag=BagTiles):
        tile_to_exchange = self.rack.pop(index)
        new_tile = bag.take(1)
        bag.put([tile_to_exchange])
        self.rack.append(new_tile)
    
    def has_letters(self, tiles):
        list_true = []
        for x in tiles:
            for y in self.rack:
                if x.letter == y.letter:
                    list_true.append(1)
        if len(list_true) == len(tiles):
            return True
        return False