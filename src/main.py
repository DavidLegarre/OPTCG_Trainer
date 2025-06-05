from src.game_state.game_state import Game
from src.game_state.main_menu_state.main_menu_state import MainMenuState
from src.game_state.play_state.play_state import PlayState


def main():
    # Example usage
    game = Game()
    main_menu = MainMenuState()
    play_state = PlayState()

    game.change_state(main_menu)
    game.update()
    game.render()

    game.change_state(play_state)
    game.update()
    game.render()


if __name__ == "__main__":
    main()
