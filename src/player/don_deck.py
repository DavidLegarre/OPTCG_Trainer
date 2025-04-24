class DonManager:
    def __init__(self):
        """
        Initialize the DON!! Manager.
        """
        self.active_don = 0
        self.rested_don = 0
        self.total_don = 10

    def add_don(self, amount):
        """
        Add DON!! cards to the active pool (e.g., during the DON!! Phase).
        :param amount: Number of DON!! cards to add.
        """
        if self.total_don + amount > 10:
            amount = 10 - self.total_don  # Cap at the maximum limit of 10 DON!!
        self.active_don += amount
        self.total_don += amount
        print(f"Gained {amount} DON!! cards. Total active DON!!: {self.active_don}.")

    def rest_don(self, amount):
        """
        Rest DON!! cards to pay a cost.
        :param amount: Number of DON!! cards to rest.
        :return: True if successful, False if not enough active DON!!.
        """
        if self.active_don >= amount:
            self.active_don -= amount
            self.rested_don += amount
            print(
                f"Rested {amount} DON!! cards. Active DON!!: {self.active_don}, Rested DON!!: {self.rested_don}."
            )
            return True
        else:
            print(
                f"Not enough active DON!! cards to rest. Needed: {amount}, Available: {self.active_don}."
            )
            return False

    def reset_don(self):
        """
        Reset all rested DON!! cards to active during the Refresh Phase.
        """
        self.active_don += self.rested_don
        self.rested_don = 0
        print(
            f"All rested DON!! cards have been reset. Active DON!!: {self.active_don}."
        )

    def attach_don(self, card, amount):
        """
        Attach DON!! cards to a Leader or Character card for bonus power.
        :param card: The card to attach the DON!! cards to.
        :param amount: Number of DON!! cards to attach.
        :return: True if successful, False if not enough active DON!!.
        """
        if self.active_don >= amount:
            self.active_don -= amount
            card.attached_don += amount
            print(
                f"Attached {amount} DON!! cards to {card.name}. Active DON!!: {self.active_don}."
            )
            return True
        else:
            print(
                f"Not enough active DON!! cards to attach. Needed: {amount}, Available: {self.active_don}."
            )
            return False

    def return_don(self, card):
        """
        Return all DON!! cards attached to a card back to the cost area as rested.
        :param card: The card whose DON!! cards are being returned.
        """
        self.rested_don += card.attached_don
        print(
            f"Returned {card.attached_don} DON!! cards from {card.name} to the cost area."
        )
        card.attached_don = 0
