# Blackjack game, 1 user vs the computer

This is a CLI game of blackjack in which most of the real world behaviors have been implemented.
It is designed to work on OOP methodology. Each class has properties and behaviors which are specific and can impact objects of the others class at runtime (when a player has reached the end of a hand the dealer's hand is also reset)


The dealer has very specific tasks to accomplish and will make decisions based on it's hand, the hand of the player and the table rules (must hit 16 and below).

See below a play example:
```python
Welcome to Blackjack!


You are starting with $500. Would you like to play a hand? yes
Place your bet: 600
Too high, you only have $500.
Place your bet: a 
Not valid, your bet has to be an integer.
Place your bet: -5
Min bet is $1.
Place your bet: 13
You are dealt: J♦, A♣
The dealer is dealt: 7♦, Unknown
The dealer has: 7♦ 2♦ 
Blackjack! You win $39 :)

You are starting with $526. Would you like to play a hand? y
Place your bet: 20
You are dealt: 3♠, 7♣
The dealer is dealt: 5♥, Unknown
Would you like to hit or stay? hit
You are dealt: 7♥
You now have: 3♠ 7♣ 7♥ 
Would you like to hit or stay? stay
The dealer has: 5♥ 5♣ 
Dealer hits, and is dealt: 2♥
The dealer has: 5♥ 5♣ 2♥ 
Dealer hits, and is dealt: 4♦
The dealer has: 5♥ 5♣ 2♥ 4♦ 
Dealer hits, and is dealt: 6♣
The dealer has: 5♥ 5♣ 2♥ 4♦ 6♣ 
The dealer busts
You win $40!

You are starting with $546. Would you like to play a hand? Yes
Place your bet: 100
You are dealt: 6♠, 6♥
The dealer is dealt: 9♦, Unknown
Would you like to hit or stay? hit
You are dealt: 8♣
You now have: 6♠ 6♥ 8♣ 
Would you like to hit or stay? stay
The dealer has: 9♦ A♦ 
The dealer stays.
You tie. Your bet of $100 has been returned.

The deck has been shuffled!!

You are starting with $546. Would you like to play a hand? YES
Place your bet: 100
You are dealt: J♠, A♥
The dealer is dealt: 10♦, Unknown
The dealer has: 9♦ Q♦ 
Blakjack! You win $300!


You are starting with $746. Would you like to play a hand? neah
Ok, goodbye!
```


## Notes:
Inputs have been limited to 10 tries to get a correct input.
egg. for the bet input, it has to be an integer higher than $1 and within the limit of the money the player has

A deck shuffle function has been implemented to mimic the real behavior of a dealer.
In real-life the dealer inserts a special card somewhere random inside the deck.
Once this special card is reached, the given hand is finished, then the deck is shuffled.
The program does the same thing. As in real-life the special card cannot be to close to the bottom of the deck or the play runs into the risk of not having enough cad for the hand. 

Splits, doubles and insurance are 3 rare functions of the game which are to be implemented in the future.