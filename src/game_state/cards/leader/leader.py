from dataclasses import dataclass

from src.game_state.cards.base import BaseCard, CardType, CardAttribute, CardColor, BaseCardData
from src.game_state.cards.effect import BaseEffect


@dataclass
class LeaderCardData:
    life: int
    base_power: int
    attribute: CardAttribute
    effects: BaseEffect


class LeaderCard(BaseCard):

    def __init__(self, base_data: BaseCardData, leader_data: LeaderCardData):
        super().__init__(base_data)
        self._leader_data: LeaderCardData = leader_data

        self.current_power: int = leader_data.base_power

    def get_type(self):
        pass

    def get_cost(self):
        pass

    def get_color(self):
        pass
