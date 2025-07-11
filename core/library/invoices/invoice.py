class Invoice():
    def __init__(self):
        self.charges = []
        self.total_charges = 0

        self.payments = []
        self.total_payments = 0
        pass

    def __getitem__(self, key):
        """Allows access to the invoice attributes like a dictionary."""
        return getattr(self, key, None)

    def get_movements(self):
        """Returns a list of all movements, including charges and payments."""
        output = []
        output.extend(self.charges)
        output.extend(self.payments)
        return output