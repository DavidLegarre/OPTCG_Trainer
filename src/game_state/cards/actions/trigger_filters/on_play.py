import re
from typing import List

from src.game_state.cards.actions.trigger import Trigger
from src.game_state.cards.effect import Effect


def on_play_filter(card_text: str) -> List[Effect]:
    effects = []
    match = re.search(r"\[\s*on\s+play\s*\](.*)", card_text, flags=re.IGNORECASE)
    if not match:
        return effects

    body = match.group(1).strip()

    # Example sub-effect: draw cards
    m = re.search(r"draw (\d+) cards?", body)
    if m:
        count = int(m.group(1))

        def action(game_state, source_card, player):
            print(f"{player.name} draws {count} cards.")
            # TODO: implement logic

        effects.append(Effect(trigger=Trigger.ON_PLAY, action=action))

    return effects
