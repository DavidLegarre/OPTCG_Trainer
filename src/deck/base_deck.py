from src.deck.card.base_card import BaseCard


class BaseDeck:
    def __init__(self, cards: list[BaseCard]):
        self._cards = cards
