"""
Blackjack Game
Austin Bly, 2022
"""


from deck_fns import new_deck, deal_cards
from hit_fns import player_hit, dealer_hit
from show_fns import show_player_cards, show_dealer_cards
from bust_fns import sum_cards_ace_high
import time

show_dealer = False

"""
First deal

Initiation of the game. A randomly shuffled deck is acquired and dealt to the player and dealer.
"""

current_deck = new_deck() # Get a new deck of shuffled cards.

(player_cards, dealer_cards, current_deck) = deal_cards(current_deck) # Deal cards to player and dealer.

# Show the player's two cards and the dealer's second card
show_player_cards(player_cards)

show_dealer_cards(dealer_cards,show_dealer)


"""
Player's turn

The player decides whether to hit or stay. They continue making this decision until they either bust or stay.
"""

player_action = ""
player_choices = ["h", "s"] # Identify potential user choices


while player_action not in player_choices or player_action != "s": # Ensure user gives valid input or is not "staying".

    player_action = input("Hit or stay? (H/S): ").lower()

    if player_action == "h":
        (current_deck, player_cards) = player_hit(current_deck, player_cards)
    elif player_action == "s":
        pass
    else:
        pass

    show_player_cards(player_cards)

    if sum_cards_ace_high(player_cards) > 21:
        print("Player busts, dealer wins!")
        break
    else:
        pass


"""Dealer hits until exceed 17 or bust"""
time.sleep(3)

show_dealer = True
show_dealer_cards(dealer_cards, show_dealer)

time.sleep(3)

while sum_cards_ace_high(dealer_cards) < 17:
    (current_deck, dealer_cards) = dealer_hit(current_deck, dealer_cards)
    print("Dealer hits!", end = " ")
    show_dealer_cards(dealer_cards, show_dealer)
    time.sleep(3)

if sum_cards_ace_high(dealer_cards) > 21:
    print("Dealer busts!")
else:
    pass

# """Game Result"""
#
# if hand_status(player_cards)[1] > hand_status(dealer_cards)[1]:
#     print(
#         "Player wins with {p} over dealer total of {d}".format(
#             p=hand_status(player_cards)[1], d=hand_status(dealer_cards)[1]
#         )
#     )
# elif hand_status(player_cards)[1] < hand_status(dealer_cards)[1]:
#     print(
#         "Dealer wins with {d} over player total of {p}".format(
#             p=hand_status(player_cards)[1], d=hand_status(dealer_cards)[1]
#         )
#     )
# else:
#     print(
#         "Push! Dealer has {d} and player has {p}".format(
#             d=hand_status(dealer_cards)[1], p=hand_status(player_cards)[1]
#         )
#     )
