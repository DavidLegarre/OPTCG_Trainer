from src.game_state.game_state import GameState


class PlayState(GameState):
    def enter(self):
        print("Entering Play State")

    def exit(self):
        print("Exiting Play State")

    def update(self):
        print("Updating Play State")

    def render(self):
        print("Rendering Play State")
