from src.game_state.game_state import GameState


class PlayState(GameState):
    def enter(self):
        print("Entering Play State")

    def handle_input(self):
        user_input = (
            input("Play State > Press 'q' to quit, 'c' to continue: ").strip().lower()
        )
        if user_input == "q":
            self.game.running = False  # Exit game loop
        elif user_input == "c":
            print("Continuing...")  # No state change, just continues
        else:
            print("Unknown command.")

    def update(self):
        print("Updating Play State")

    def render(self):
        print("Rendering Play State")
