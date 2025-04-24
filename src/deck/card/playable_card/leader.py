from src.deck.card.base_card import BaseCardData, Card


class LeaderCard(Card):
    def __init__(self, data: BaseCardData, life: int, power: int):
        super().__init__(data)
        self.life = life
        self.power = power
        self.attached_don = 0
