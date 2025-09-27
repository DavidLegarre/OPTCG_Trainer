from abc import ABC, abstractmethod

from src.game_state.cards.base import BaseCard


class BaseDeck(ABC):
    @abstractmethod
    def draw(self, number_cards: int):
        ...

    @abstractmethod
    def shuffle(self):
        pass

    @abstractmethod
    def add_to_top(self, card: BaseCard):
        ...

    @abstractmethod
    def add_to_bottom(self, card: BaseCard):
        ...
