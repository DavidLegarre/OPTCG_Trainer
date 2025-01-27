class GameBoard:
    def __init__(self):
        self.leader_area = None  # The Leader card
        self.character_area = []  # Character cards on the field
        self.stage_area = None  # A single Stage card
        self.cost_area = []  # Active/rested DON!! cards
        self.life_area = []  # Face-down Life cards
        self.trash_area = []  # Discard pile
