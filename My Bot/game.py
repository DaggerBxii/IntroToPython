#game.py
from player import Player

class Game:
    def __init__(self):
        self.players = {} 
def getPlayer(self, player_id):
    none_var = None
    player = self.players.get(player_id)
    if player is not none_var:
        return player
    else:
        self.players[player_id] = Player(player_id, 0, 2, 10)
        return self.players[player_id]