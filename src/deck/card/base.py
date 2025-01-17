from typing import Optional
from src.effects.base import BaseCardEffect


class BaseCard:
    def __init__(
        self,
        name,
        description,
        id: int,
        category: str,
        color: Optional[str | list[str]],
        type: Optional[str],
        effects: Optional[list[BaseCardEffect]],
    ):
        self.name = name
        self.description = description
        self.id = id
        self.category = category
        self.color = color
