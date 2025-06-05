class Effect:
    def __init__(self, trigger, action):
        self.trigger = trigger
        self.action = action

    def resolve(self, game_state, source_card, player, target):
        self.action(game_state, source_card, player, target)
