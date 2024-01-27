#player.py
class Player:
    def __init__(self, id, xp=0, attack=0, hp=0):
        self.id = id
        self.xp = xp
        self.attack = attack
        self.max_hp = hp
        self.current_hp = hp
        