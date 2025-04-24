from src.deck.card.base_card import Card


class PlayableCard(Card):
    def __init__(self, data, power):
        super().__init__(data)
        self._power = power
        self._attached_don = 0

    def attach_don(self, don):
        self._attached_don += don

    def detach_don(self, don):
        self._attached_don -= don

    def reset_don(self):
        self._attached_don = 0

    def calculate_power(self):
        return self._power + (self._attached_don * 1000)
