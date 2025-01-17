from src.card.base import BaseCard


class LeaderCard(BaseCard):
    def __init__(
        self,
        power: int,
        life: int,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.power = power
        self.life = life
