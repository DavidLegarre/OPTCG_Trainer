class BaseCardEffect:
    def __init__(self, name, description, trigger, cost=None, *args, **kwargs):
        self.name = name
        self.description = description
        self.trigger = trigger
        self.cost = cost

    def activate(self, game_state, **kwargs):
        raise NotImplementedError
