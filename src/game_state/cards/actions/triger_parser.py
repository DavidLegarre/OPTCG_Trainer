from src.game_state.cards.actions.trigger_filters.on_play import on_play_filter
from src.game_state.cards.actions.trigger_filters.when_attacking import (
    when_attacking_filter,
)
from src.game_state.cards.effect import Effect


def parse_effects(card_text: str) -> list[Effect]:
    effects = []

    text = card_text.strip().lower()

    # Call all modular filters that return a list of Effect objects
    all_filters = [on_play_filter, when_attacking_filter]

    effects = []
    for filter_fn in all_filters:
        effects.extend(filter_fn(text))

    return effects
