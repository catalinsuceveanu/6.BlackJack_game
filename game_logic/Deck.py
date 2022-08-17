import random


class Deck:
    full_deck = (
        ["♦", "2"],
        ["♥", "2"],
        ["♣", "2"],
        ["♠", "2"],
        ["♦", "3"],
        ["♥", "3"],
        ["♣", "3"],
        ["♠", "3"],
        ["♦", "4"],
        ["♥", "4"],
        ["♣", "4"],
        ["♠", "4"],
        ["♦", "5"],
        ["♥", "5"],
        ["♣", "5"],
        ["♠", "5"],
        ["♦", "6"],
        ["♥", "6"],
        ["♣", "6"],
        ["♠", "6"],
        ["♦", "7"],
        ["♥", "7"],
        ["♣", "7"],
        ["♠", "7"],
        ["♦", "8"],
        ["♥", "8"],
        ["♣", "8"],
        ["♠", "8"],
        ["♦", "9"],
        ["♥", "9"],
        ["♣", "9"],
        ["♠", "9"],
        ["♦", "10"],
        ["♥", "10"],
        ["♣", "10"],
        ["♠", "10"],
        ["♦", "A"],
        ["♥", "A"],
        ["♣", "A"],
        ["♠", "A"],
        ["♦", "J"],
        ["♥", "J"],
        ["♣", "J"],
        ["♠", "J"],
        ["♦", "Q"],
        ["♥", "Q"],
        ["♣", "Q"],
        ["♠", "Q"],
        ["♦", "K"],
        ["♥", "K"],
        ["♣", "K"],
        ["♠", "K"],
    )

    def __init__(self):
        full_deck_list = list(Deck.full_deck)
        random.shuffle(full_deck_list)
        self._curr_deck = full_deck_list
        self._curr_card_idx = 0

    def deal_a_card(self):
        curr_card = self.curr_deck[self.curr_card_idx]
        self.curr_card_idx += 1
        return curr_card

    @property
    def curr_deck(self):
        return self._curr_deck

    @curr_deck.setter
    def curr_deck(self, new_deck):
        self._curr_deck = new_deck

    @property
    def curr_card_idx(self):
        return self._curr_card_idx

    @curr_card_idx.setter
    def curr_card_idx(self, value):
        self._curr_card_idx = value

    def shuffle_the_deck(self):
        random.shuffle(self.curr_deck)
        self.curr_card_idx = 0
