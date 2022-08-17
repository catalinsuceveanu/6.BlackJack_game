class Player:
    BLACKJACK_FACTOR = 3

    def __init__(self):
        self._cash = 500
        self._curr_bet = 0
        self._curr_deal = []

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, amount):
        self._cash = amount

    @property
    def curr_bet(self):
        return self._curr_bet

    @curr_bet.setter
    def curr_bet(self, bet):
        self._curr_bet = bet
        self.cash -= self.curr_bet

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

    def has_won(self):
        self.cash += self.curr_bet * 2
        self.curr_bet = 0
        self.curr_deal.clear()

    def has_lost(self):
        self.curr_bet = 0
        self.curr_deal.clear()

    def its_a_draw(self):
        self.cash += self.curr_bet
        self.curr_deal.clear()

    def has_blackjack(self):
        self.cash += int(self.curr_bet * Player.BLACKJACK_FACTOR)
        self.curr_bet = 0
        self.curr_deal.clear()
