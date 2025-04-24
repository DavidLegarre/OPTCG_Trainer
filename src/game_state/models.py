from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Dict


class Zone(Enum):
    DECK = auto()
    HAND = auto()
    DISCARD = auto()
    IN_PLAY = auto()


@dataclass
class Card:
    card_id: str
    name: str
    cost: int
    color: str
    type: str
    power: int
    ability: str
    image_url: str


@dataclass
class Player:
    name: str
    deck: List[Card] = field(default_factory=list)
    hand: List[Card] = field(default_factory=list)
    discard: List[Card] = field(default_factory=list)
    in_play: List[Card] = field(default_factory=list)


@dataclass
class GameState:
    players: Dict[str, Player]
    turn_player: str
    turn_number: int = 1
    phase: str = "draw"
