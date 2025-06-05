from src.game_state.game_state import GameState
from src.game_state.play_state.play_state import PlayState


class MainMenuState(GameState):
    def enter(self):
        print("Entering Main Menu")

    def handle_input(self):
        user_input = input("Press 'p' to play or 'q' to quit: ")
        if user_input == "p":
            self.game.state = PlayState(self.game)
            self.game.state.enter()
        elif user_input == "q":
            self.game.running = False

    def update(self):
        pass

    def render(self):
        print("Main Menu Rendering...")
