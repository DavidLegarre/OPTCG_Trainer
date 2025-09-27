from dataclasses import dataclass

from src.game_state.cards.base import BaseCard, CardType, CardAttribute, CardColor

@dataclass
class LeaderCardData:
    life: int
    base_power: int


class LeaderCard(BaseCard):

    def __init__(self, card_color: CardColor, power: int, attribute: CardAttribute):
        super().__init__(CardType.LEADER, card_color)
        self._power: int = power
        self._attribute: CardAttribute = attribute

    def get_type(self):
        pass

    def get_cost(self):
        pass

    def get_color(self):
        pass
