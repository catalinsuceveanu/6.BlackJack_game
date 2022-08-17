class Dealer:
    STAY_SUM = 17

    def __init__(self):
        self._curr_deal = []

    @property
    def curr_deal(self):
        return self._curr_deal

    @curr_deal.setter
    def curr_deal(self, cards):
        self._curr_deal = cards

    def add_card_to_curr_deal(self, card):
        new_cards = self.curr_deal
        new_cards.append(card)
        self.curr_deal = new_cards

    def reset_curr_deal(self):
        self.curr_deal.clear()
