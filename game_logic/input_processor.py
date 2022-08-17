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
    tries = 10
    while tries > 0:
        response = input("Place your bet: ")
        tries -= 1
        try:
            response = int(response)
            if response <= 0:
                raise custom_errors.SubZeroBetError()
            elif response > amount:
                raise custom_errors.BetHigherThanAmountError()
            else:
                return response
        except ValueError:
            print("Not valid, your bet has to be an integer.")
        except custom_errors.SubZeroBetError:
            print("Not a valid bet, please place a bet higher than $0.")
        except custom_errors.BetHigherThanAmountError:
            print(f"Too high, you only have ${amount}.")
    print("Ran out of tries, restart the game to play again.")


get_a_bet = place_your_bet(500)
print("Your bet is", get_a_bet)
