from src.deck.card.base_card import Card


class BaseDeck:
    def __init__(self, cards: list[Card]):
        self._cards = cards
