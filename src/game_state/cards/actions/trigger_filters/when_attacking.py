import re

from src.game_state.cards.actions.trigger import Trigger


def when_attacking_filter(card_text: str):
    match = re.search(r"\[when attacking]", card_text, flags=re.IGNORECASE)
    if not match:
        return []

    return Trigger.WHEN_ATTACKS
