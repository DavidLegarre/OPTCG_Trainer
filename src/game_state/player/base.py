from src.game_state.board.base import BaseBoard
from src.game_state.deck.base import BaseDeck


class BasePlayer:
    def __init__(self, deck: BaseDeck):
        self._deck: BaseDeck = deck
        self._board: BaseBoard
