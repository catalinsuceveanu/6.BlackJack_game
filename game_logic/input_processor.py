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
            if response < 1:
                raise custom_errors.SubZeroBetError()
            elif response > amount:
                raise custom_errors.BetHigherThanAmountError()
            else:
                return response
        except ValueError:
            print("Not valid, your bet has to be an integer.")
        except custom_errors.SubZeroBetError:
            print("Min bet is $1.")
        except custom_errors.BetHigherThanAmountError:
            print(f"Too high, you only have ${amount}.")
    print("Ran out of tries, restart the game to play again.")


def want_to_hit_or_stay():
    stay_responses = ("stay", "Stay", "STAY", "s", "S")
    hit_responses = ("hit", "Hit", "HIT", "h", "H")
    tries = 5
    while tries > 0:
        response = input("Would you like to hit or stay? ")
        if response in stay_responses:
            return False
        elif response in hit_responses:
            return True
        else:
            print("Not a valid input, try again!")
            tries -= 1
