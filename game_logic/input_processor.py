import custom_errors


def initiate_hand(amount):
    response = input(
        f"You are starting with ${amount}. Would you like to play a hand? "
    )
    acceptable_responses = ("yes", "Yes", "YES", "y", "Y")
    if response in acceptable_responses:
        return True
    else:
        print("Ok, goodbye!")


def place_your_bet(amount):
    bet = None
    while True:
        response = input("Place your bet: ")
        try:
            response = int(response)
            if response <= 0:
                raise custom_errors.SubZeroBetError()
            elif response > amount:
                raise custom_errors.BetHigherThanAmountError()
            else:
                bet = response
                break
        except ValueError:
            print("Not valid, your bet has to be an integer.")
        except custom_errors.SubZeroBetError:
            print("Not a valid bet, please place a bet higher than $0.")
        except custom_errors.BetHigherThanAmountError:
            print(f"Too high, you only have ${amount}.")
    return bet


get_a_bet = place_your_bet(500)
print("Your bet is", get_a_bet)
