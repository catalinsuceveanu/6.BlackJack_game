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
        if has_blackjack(player):
            print_curr_deal(dealer)
            if deal_total(dealer) != 21:
                player.has_blackjack(dealer)
            else:
                player.its_a_draw(dealer)

        else:
            curr_player_deal_total = deal_total(player)
            player_wants_to_hit = input_processor.wants_to_hit()
            while curr_player_deal_total <= 21 and player_wants_to_hit == True:
                player.add_card_to_curr_deal(deck.deal_a_card())
                print_the_new_dealt_card(player)
                curr_player_deal_total = deal_total(player)
                if curr_player_deal_total > 21:
                    break
                player_wants_to_hit = input_processor.wants_to_hit()
            if curr_player_deal_total > 21:
                print(f"Your hand value is over 21.")
                player.has_lost(dealer)
            else:
                dealer_total = deal_total(dealer)
                print_curr_deal(dealer)
                while dealer_total < Dealer.STAY_SUM:
                    dealer.add_card_to_curr_deal(deck.deal_a_card())
                    print_the_new_dealt_card(dealer)
                    dealer_total = deal_total(dealer)
                if dealer_total > 21:
                    print(f"The dealer busts")
                    player.has_won(dealer)
                else:
                    print("The dealer stays.")
                    if curr_player_deal_total > dealer_total:
                        player.has_won(dealer)
                    elif curr_player_deal_total == dealer_total:
                        player.has_tied(dealer)
                    else:
                        player.has_lost(dealer)
        if deck.curr_card_idx >= deck.shuffle_card:
            deck.shuffle_the_deck()
        playing = input_processor.initiate_hand(player.cash)


def deal_cards(player, dealer, deck):
    for i in range(1, 5):
        if i % 2 == 0:
            player.add_card_to_curr_deal(deck.deal_a_card())
        else:
            dealer.add_card_to_curr_deal(deck.deal_a_card())


def print_initial_deal(player, dealer):
    print(
        f"You are dealt: {player.curr_deal[0][1]}{player.curr_deal[0][0]}, {player.curr_deal[1][1]}{player.curr_deal[1][0]}"
    )
    print(
        f"The dealer is dealt: {dealer.curr_deal[0][1]}{dealer.curr_deal[0][0]}, Unknown"
    )


def print_curr_deal(entity):
    if isinstance(entity, Player):
        to_print = "You now have: "
        for card in entity.curr_deal:
            to_print += card[1] + card[0] + " "
        print(to_print)
    elif isinstance(entity, Dealer):
        to_print = "The dealer has: "
        for card in entity.curr_deal:
            to_print += card[1] + card[0] + " "
        print(to_print)


def print_the_new_dealt_card(entity):
    last_card = entity.curr_deal[-1]
    last_card_string = last_card[1] + last_card[0]
    if isinstance(entity, Player):
        print(f"You are dealt: {last_card_string}")
        print_curr_deal(entity)
    elif isinstance(entity, Dealer):
        print(f"Dealer hits, and is dealt: {last_card_string}")
        print_curr_deal(entity)


def has_blackjack(player):
    if deal_total(player) == 21:
        return True
    else:
        return False


def deal_total(entity):
    """The method looks at all the cards in a deal (player or dealer) and adds up the total count.
    The special function a Ace has is that it can be either a 1, or an 11.
    The method first adds up the maximum value possible (Aces = 11) and counts the no of Aces.
    Then if total count is higher than 21 (called a bust), it transforms all the Aces, one by one,
    into value 1. Until, of course we ran out of aces. Finally returns the best possible total for
    a given deal."""
    total = 0
    no_of_aces = 0
    for card in entity.curr_deal:
        card_value = card[1]
        total += Deck.Deck.equivalent_values[card_value]
        if card_value == "A":
            no_of_aces += 1
    while total > 21:
        if no_of_aces > 0:
            total -= 10
            no_of_aces -= 1
        else:
            break
    return total


if __name__ == "__main__":
    main()
