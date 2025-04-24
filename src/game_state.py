from enum import Enum


class Phase(Enum):
    DRAW = 0
    MAIN = 1
    COMBAT = 2
    END = 3


class GameState:
    def __init__(self):
        self.players = []
        self.current_player = None
        self.current_opponent = None
        self.turn_number = 0
        self.game_over = False
