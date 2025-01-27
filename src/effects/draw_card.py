from src.effects.base_effect import BaseCardEffect


class DrawCardEffect(BaseCardEffect):
    def __init__(
        self, name, description, trigger, cost=None, draw_amount=1, *args, **kwargs
    ):
        super().__init__(name, description, trigger, cost, *args, **kwargs)
        self.draw_amount = draw_amount

    def activate(self, game_state, player):
        """
        Logic to draw cards from the player's deck.
        """
        for _ in range(self.draw_amount):
            if player.deck:
                drawn_card = player.deck.pop(0)
                player.hand.append(drawn_card)
                print(f"{player.name} draws {drawn_card.name}.")
            else:
                print(f"{player.name}'s deck is empty.")
