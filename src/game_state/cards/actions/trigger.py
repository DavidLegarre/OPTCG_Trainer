from enum import Enum, auto


class Trigger(Enum):
    ON_PLAY = auto()  # [On Play]
    WHEN_ATTACKS = auto()  # [When Attacking]
    ON_KO = auto()  # [On KO]
    ON_BLOCK = auto()  # [On Block] (hypothetical, rarely used)
    START_OF_TURN = auto()  # [At the start of your turn]
    END_OF_TURN = auto()  # [At the end of your turn]
    ACTIVATE_MAIN = auto()  # [Main] or [Activate:Main]
    ACTIVATE_BATTLE = auto()  # [Battle] or [Activate:Battle]
    ON_COUNTER = auto()  # [Counter]
    ON_TRIGGER = auto()  # [Trigger] – when revealed from life
    ON_DON_ATTACHMENT = auto()  # [When this card is given DON!!]
    ON_OPPONENT_PLAY = auto()  # [When your opponent plays a card]
    ON_ATTACK_TARGET = auto()  # [When this card is attacked]
    ON_OPPONENT_ATTACK = auto()  # [When your opponent attacks]
    ON_DON_REMOVED = auto()  # [When DON!! is removed from this card]

    # Optional for deckbuilding/game zones
    ON_DRAW = auto()
    ON_REST = auto()
    ON_ACTIVE = auto()
