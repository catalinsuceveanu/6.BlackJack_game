from Player import Player
from Dealer import Dealer
import input_processor
import Deck


def main():
    print("Welcome to Blackjack!\n")
    player = Player()
    dealer = Dealer()
    deck = Deck.Deck()
    playing = input_processor.initiate_hand(player.cash)

    while playing:
        player.curr_bet = input_processor.place_your_bet(player.cash)
        deal_cards(player, dealer, deck)
        print_initial_deal(player, dealer)
        hand_total(dealer)
        hand_total(player)

        playing = input_processor.initiate_hand(player.cash)


def deal_cards(player, dealer, deck):
    player.add_card_to_curr_deal(deck.deal_a_card())
    dealer.add_card_to_curr_deal(deck.deal_a_card())
    player.add_card_to_curr_deal(deck.deal_a_card())
    dealer.add_card_to_curr_deal(deck.deal_a_card())


def print_initial_deal(player, dealer):
    print(
        f"You are dealt: {player.curr_deal[0][1]}{player.curr_deal[0][0]}, {player.curr_deal[1][1]}{player.curr_deal[1][0]}"
    )
    print(
        f"The dealer is dealt: {dealer.curr_deal[0][1]}{dealer.curr_deal[0][0]}, Unknown"
    )


def has_blackjack():
    pass


def hand_total(entity):
    total = 0
    no_of_aces = 0
    for card in entity.curr_deal:
        card_value = card[1]
        total += Deck.Deck.equivalent_values[card_value]
        if card_value == "A":
            no_of_aces += 1
    print(entity.curr_deal, total)


if __name__ == "__main__":
    main()
