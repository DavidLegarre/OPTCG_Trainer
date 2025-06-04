from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Dict, Callable, Any
import re


# --- Enums for Zones and Phases ---
class Zone(Enum):
    DECK = auto()
    HAND = auto()
    DISCARD = auto()
    IN_PLAY = auto()
    STACK = auto()  # for effects waiting to resolve


class Phase(Enum):
    DRAW = auto()
    MAIN = auto()
    ATTACK = auto()
    END = auto()


# --- Base Classes for Effects and Abilities ---
@dataclass
class Effect:
    """
    Represents a single effect that can modify the game state.
    """

    description: str
    execute: Callable[["GameState", "Ability", Any], None]


@dataclass
class Ability:
    """
    Represents a triggered or activated ability of a card, parsed from its text.
    """

    trigger: str  # e.g., "On Play", "When Attacks"
    cost: Dict[str, Any]  # e.g., {"rest": True, "energy": 1}
    effects: List[Effect]


# --- Card and Player ---
@dataclass
class Card:
    card_id: str
    name: str
    cost: int
    color: str
    type: str
    power: int
    raw_text: str
    image_url: str = ""
    abilities: List[Ability] = field(default_factory=list)

    def parse_abilities(self):
        """
        Parses raw_text into Ability objects.
        Simplistic regex-based parser for common patterns.
        """
        lines = [line.strip() for line in self.raw_text.split(".") if line]
        for line in lines:
            # Example: "On Play: Draw 2 cards"
            m = re.match(r"On Play: (.*)", line, re.IGNORECASE)
            if m:
                desc = m.group(1)
                # simple effect: draw N cards
                draw_m = re.match(r"Draw (\d+) cards?", desc, re.IGNORECASE)
                if draw_m:
                    n = int(draw_m.group(1))

                    def effect_fn(state, ability, target=None, n=n):
                        state.draw_cards(state.active_player, n)

                    eff = Effect(description=desc, execute=effect_fn)
                    abl = Ability(trigger="On Play", cost={}, effects=[eff])
                    self.abilities.append(abl)
            # Extend here with more patterns: When Attacks, When KO, etc.


# --- Player and GameState ---
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
    phase: Phase = Phase.DRAW
    stack: List[Ability] = field(default_factory=list)

    @property
    def active_player(self) -> Player:
        return self.players[self.turn_player]

    def draw_cards(self, player: Player, n: int):
        for _ in range(n):
            if not player.deck:
                break
            card = player.deck.pop(0)
            player.hand.append(card)

    def play_card(self, player: Player, card: Card):
        if card not in player.hand:
            raise ValueError("Card not in hand")
        player.hand.remove(card)
        player.in_play.append(card)
        # Trigger On Play abilities:
        for ability in card.abilities:
            if ability.trigger == "On Play":
                self.stack.append(ability)

    def resolve_stack(self):
        # Last-in, first-out
        while self.stack:
            ability = self.stack.pop()
            # execute all effects of the ability
            for eff in ability.effects:
                eff.execute(self, ability)
