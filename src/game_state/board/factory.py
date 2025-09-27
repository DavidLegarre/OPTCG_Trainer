from src.game_state.board.player_board import PlayerBoard


class BoardFactory:
    @staticmethod
    def default_board() -> PlayerBoard:
        board = PlayerBoard()
        # If you want defaults, e.g. initial stages:
        # board.add_stage("Stage1")
        # board.add_stage("Stage2")
        # but maybe leave characters empty
        return board

    @staticmethod
    def custom_board(max_characters: int, max_stages: int, initial_stages: List[str] = None) -> PlayerBoard:
        board = PlayerBoard(max_characters=max_characters, max_stages=max_stages)
        if initial_stages:
            for st in initial_stages:
                board.add_stage(st)
        return board
