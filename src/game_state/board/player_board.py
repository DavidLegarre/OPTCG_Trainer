from src.game_state.board.base import BaseBoard
from src.game_state.cards.character.base import BaseCharacterCard
from src.game_state.cards.stage.stage import BaseStageCard


class PlayerBoard(BaseBoard):
    def __init__(self):
        self._characters: list[BaseCharacterCard] = []
        self._stage: BaseStageCard | None = None

    @property
    def characters(self) -> list[BaseCharacterCard]:
        return list(self._characters)

    @property
    def stage(self) -> BaseStageCard:
        return self._stage

    def add_character(self, character: BaseCharacterCard):
        self._characters.append(character)

    def remove_character(self, character: BaseCharacterCard):
        if character in self._characters:
            self._characters.remove(character)

    def add_stage(self, stage: BaseStageCard):
        self._stage = stage

    def remove_stage(self):
        self._stage = None
