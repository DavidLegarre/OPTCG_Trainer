from abc import ABC, abstractmethod


class GameState(ABC):
    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass


class Game:
    def __init__(self):
        self.state = None

    def change_state(self, new_state):
        if self.state is not None:
            self.state.exit()
        self.state = new_state
        self.state.enter()

    def update(self):
        if self.state is not None:
            self.state.update()

    def render(self):
        if self.state is not None:
            self.state.render()
