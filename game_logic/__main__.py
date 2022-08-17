import Player
import input_processor
import Deck


def main():
    print("Welcome to Blackjack!\n")
    player = Player()
    deck = Deck()
    playing = input_processor.initiate_hand(player.cash)
    while playing:
        curr_bet = input_processor.place_your_bet(player.cash)
        curr_hand = [deck.deal_a_card(), de]

        playing = input_processor.initiate_hand(player.cash)


def hand_total(cards):
    pass


if __name__ == "__main__":
    main()
