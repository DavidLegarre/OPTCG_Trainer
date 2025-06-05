from src.game_state.game_state import GameState


class MainMenuState(GameState):
    def enter(self):
        print("Entering Main Menu")

    def exit(self):
        print("Exiting Main Menu")

    def update(self):
        print("Updating Main Menu")

    def render(self):
        print("Rendering Main Menu")
