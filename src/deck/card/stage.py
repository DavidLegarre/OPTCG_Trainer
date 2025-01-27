from src.deck.card.base_card import BaseCardData, Card


class StageCard(Card):
    def __init__(self, data: BaseCardData):
        super().__init__(data)
