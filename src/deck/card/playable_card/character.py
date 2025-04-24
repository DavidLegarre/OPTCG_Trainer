from src.deck.card.base_card import Card


class CharacterCard(Card):
    def __init__(self, name, cost, color, power, counter, effects=None):
        super().__init__(name, "Character", cost, color, effects)
        self.power = power
        self.counter = counter
        self.attached_don = 0
