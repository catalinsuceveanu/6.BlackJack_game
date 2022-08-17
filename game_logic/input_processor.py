def initiate_hand(amount):
    response = input(
        f"You are starting with ${amount}. Would you like to play a hand? "
    )
    acceptable_responses = ("yes", "Yes", "YES", "y", "Y")
    if response in acceptable_responses:
        return True
    else:
        print("Ok, goodbye!")
