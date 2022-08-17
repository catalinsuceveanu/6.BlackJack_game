class SubZeroBetError(Exception):
    """Not a valid bet, please place a bet higher than 0"""

    pass


class BetHigherThanAmountError(Exception):
    """Not a valid bet, please place a bet lower than your amount"""

    pass
