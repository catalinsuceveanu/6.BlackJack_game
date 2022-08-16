class Player:
    def __init__(self):
        self._cash = 500

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, amount):
        self._cash += amount
