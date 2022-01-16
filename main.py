"""
Blackjack Game
Austin Bly, 2022
"""


from card_fns import new_deck, deal_cards
from hit_fns import player_hit, dealer_hit, hand_status

"""
First deal

Initiation of the game. A randomly shuffled deck is acquired and dealt to the player and dealer.
"""

current_deck = new_deck() # Get a new deck of shuffled cards.

(player_cards, dealer_cards, current_deck) = deal_cards(current_deck) # Deal cards to player and dealer.

# Show the player's two cards and the dealer's second card
print("Player cards are: ", player_cards)
print("Dealer is showing: ", dealer_cards[1])

"""
Player's turn
 
The player decides whether to hit or stay. They continue making this decision until they either bust or stay.
"""

player_action = ""
player_choices = ["h", "s"] # Identify potential user choices

# Ensure user gives valid input
while player_action not in player_choices or player_action != "s":

    player_action = input("Hit or stay? (H/S): ").lower()

    if player_action == "h":
        (current_deck, player_cards) = player_hit(current_deck, player_cards)
    elif player_action == "s":
        pass
    else:
        pass

    print("Player cards are:", player_cards)

    if hand_status(player_cards)[0] == True:
        print("Player busts, dealer wins!")
        break

"""Dealer hits until results"""

print("Dealer cards are", dealer_cards)

while hand_status(dealer_cards)[1] < 17:
    (current_deck, dealer_cards) = dealer_hit(current_deck, dealer_cards)
    print("Dealer hits! Dealer cards are: ", dealer_cards)

else:
    pass

"""Game Result"""

if hand_status(player_cards)[1] > hand_status(dealer_cards)[1]:
    print(
        "Player wins with {p} over dealer total of {d}".format(
            p=hand_status(player_cards)[1], d=hand_status(dealer_cards)[1]
        )
    )
elif hand_status(player_cards)[1] < hand_status(dealer_cards)[1]:
    print(
        "Dealer wins with {d} over player total of {p}".format(
            p=hand_status(player_cards)[1], d=hand_status(dealer_cards)[1]
        )
    )
else:
    print(
        "Push! Dealer has {d} and player has {p}".format(
            d=hand_status(dealer_cards)[1], p=hand_status(player_cards)[1]
        )
    )
