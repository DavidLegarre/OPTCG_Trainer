from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto


class CardColor(Enum):
    RED = "R"
    GREEN = "G"
    BLUE = "U"
    PURPLE = "P"
    BLACK = "B"
    YELLOW = "Y"


class CardType(Enum):
    LEADER = auto()
    EVENT = auto()
    CHARACTER = auto()
    STAGE = auto()


class CardAttribute(Enum):
    SLASH = auto()
    STRIKE = auto()
    SPECIAL = auto()
    WISDOM = auto()
    RANGED = auto()


@dataclass
class BaseCardData:
    type: CardType
    color: CardColor
    name: str
    card_number: str  # Card ID: STXX-XXX, OPXX-XXX, etc...


class BaseCard(ABC):
    def __init__(self, base_data: BaseCardData):
        self._base_data: BaseCardData = base_data

    def get_name(self):
        return self._base_data.name

    @abstractmethod
    def get_type(self) -> CardType:
        ...

    @abstractmethod
    def get_cost(self) -> int:
        ...

    @abstractmethod
    def get_color(self) -> CardColor:
        ...
