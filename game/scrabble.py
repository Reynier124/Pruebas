from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles
from game.miscellaneous import Miscellaneous
import uuid

class Scrabble:
    def __init__(self,player_count):
        self.board = Board()
        self.bagtiles = BagTiles()
        self.gameid = str(uuid.uuid4())
        self.players = []
        for _ in range(player_count):
            self.players.append(Player())
        self.current_player = None
        self.turn = 1
            
    def playing(self):
        return True
    
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            player_turn = self.players.index(self.current_player) + 1
            self.current_player = self.players[player_turn]
        self.turn += 1

    def validate_word(self, word, location, orientation):
        return self.board.validate_word_inside_board(word,location, orientation)
    
    def calculate_score(self, word):
        misc = Miscellaneous()
        score = misc.calculate_word_value(word)
        self.current_player.score += score