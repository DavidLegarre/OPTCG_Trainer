from src.game_state.game_base import GameBase
from src.game_state.main_menu_state.main_menu_state import MainMenuState


class Game(GameBase):
    def initialize(self):
        print("Initializing game...")
        self.running = True
        self.state = MainMenuState(self)
        self.state.enter()

    def run(self):
        self.initialize()

        while self.running:
            try:
                self.state.handle_input()
                self.state.update()
                self.state.render()
            except Exception as e:
                print(f"An error occurred: {e}")
                self.running = False

        print("Game ended.")
