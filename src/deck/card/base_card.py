from dataclasses import dataclass
from enum import Enum
from typing import Optional
from src.effects.base_effect import BaseCardEffect


class CardType(Enum):
    EVENT = "event"
    CHARACTER = "character"
    LEADER = "leader"
    STAGE = "stage"


class CardColor(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    PURPLE = "purple"
    BLACK = "black"


@dataclass
class BaseCardData:
    name: str
    description: str
    id: int
    category: str
    color: Optional[CardColor | list[CardColor]]
    card_type: CardType
    effects: Optional[list[BaseCardEffect]]


class Card:
    def __init__(self, data: BaseCardData):
        self.name = data.name
        self.description = data.description
        self.id = data.id
        self.category = data.category
        self.color = data.color
        self.card_type = data.card_type
        self.effects = data.effects
