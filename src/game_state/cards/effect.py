from typing import Callable

from src.game_state.cards.actions.trigger import Trigger


class Effect:
    def __init__(self, trigger: Trigger, action: Callable):
        self.trigger = trigger
        self.action = action

    def resolve(self, game_state, source_card, player, target):
        self.action(game_state, source_card, player, target)
