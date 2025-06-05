from src.game_state.game_base import GameBase


class GameState:
    def __init__(self, game: GameBase):
        self.game = game

    def enter(self):
        pass

    def handle_input(self):
        pass

    def update(self):
        pass

    def render(self):
        pass
