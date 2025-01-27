from dataclasses import dataclass
from typing import Optional
from src.effects.base_effect import BaseCardEffect


@dataclass
class BaseCardData:
    name: str
    description: str
    id: int
    category: str
    color: Optional[str | list[str]]
    card_type: Optional[str]
    effects: Optional[list[BaseCardEffect]]


class BaseCard:
    def __init__(self, data: BaseCardData):
        self.name = data.name
        self.description = data.description
        self.id = data.id
        self.category = data.category
        self.color = data.color
        self.card_type = data.card_type
        self.effects = data.effects
