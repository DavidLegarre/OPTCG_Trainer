from src.deck.card.base import BaseCard


class BaseDeck:
    def __init__(self, cards: list[BaseCard]):
        self._cards = cards
