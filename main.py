"""
Blackjack Game
Austin Bly, 2022
"""

import random as rand
from card_fns import new_deck, deal_cards

"""
Gameplay
"""

"""
First deal
"""
# get a new deck of cards
current_deck = new_deck()

# deal the cards
(player_cards, dealer_cards, current_deck) = deal_cards(current_deck)

# print out the player cards and second computer card
print("Player cards are: ", player_cards)
print("Dealer is showing: ", dealer_cards[1])

"""
User decisions until 'stay'
"""

hit_or_stay = ""

# repeat hit or stay process until the user 'stays'
possibilities = ["h", "s"]

# ensure user gives valid input
while hit_or_stay not in possibilities or hit_or_stay != "s":

    hit_or_stay = input("Hit or stay? (H/S): ").lower()

    if hit_or_stay == "h":
        # call player hit fn
        (current_deck, player_cards) = player_hit(current_deck, player_cards)
    elif hit_or_stay == "s":
        pass
    else:
        pass

    print("Player cards are:", player_cards)

    if bust_checker(player_cards)[0] == True:
        print("Player busts, dealer wins!")
        break

"""
Dealer hits until results
"""
print("Dealer cards are", dealer_cards)

while bust_checker(dealer_cards)[1] < 17:
    (current_deck, dealer_cards) = dealer_hit(current_deck, dealer_cards)
    print("Dealer hits! Dealer cards are: ", dealer_cards)

else:
    pass

"""
Game Result
"""

if bust_checker(player_cards)[1] > bust_checker(dealer_cards)[1]:
    print(
        "Player wins with {p} over dealer total of {d}".format(
            p=bust_checker(player_cards)[1], d=bust_checker(dealer_cards)[1]
        )
    )
elif bust_checker(player_cards)[1] < bust_checker(dealer_cards)[1]:
    print(
        "Dealer wins with {d} over player total of {p}".format(
            p=bust_checker(player_cards)[1], d=bust_checker(dealer_cards)[1]
        )
    )
else:
    print(
        "Push! Dealer has {d} and player has {p}".format(
            d=bust_checker(dealer_cards)[1], p=bust_checker(player_cards)[1]
        )
    )
