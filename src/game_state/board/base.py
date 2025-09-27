from abc import ABC, abstractmethod

from src.game_state.cards.character.base import BaseCharacterCard
from src.game_state.cards.stage.stage import BaseStageCard


class BaseBoard(ABC):
    @abstractmethod
    def add_character(self, character: BaseCharacterCard):
        pass

    @abstractmethod
    def remove_character(self, character: BaseCharacterCard):
        pass

    @abstractmethod
    def add_stage(self, stage: BaseStageCard):
        pass

    @abstractmethod
    def remove_stage(self):
        pass