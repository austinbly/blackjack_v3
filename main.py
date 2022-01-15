"""
Blackjack Game
Austin Bly, 2022
"""

import random as rand
from card_fns import new_deck


"""
Fn to deal cards to players
    -input is current deck
    -output is player cards, computer cards, and new current deck
"""
def deal_cards(current_deck):
    player_card_1 = rand.choice(current_deck)
    current_deck.remove(player_card_1)

    player_card_2 = rand.choice(current_deck)
    current_deck.remove(player_card_2)

    dealer_card_1 = rand.choice(current_deck)
    current_deck.remove(dealer_card_1)

    dealer_card_2 = rand.choice(current_deck)
    current_deck.remove(dealer_card_2)

    player_cards = [player_card_1,player_card_2]
    dealer_cards = [dealer_card_1, dealer_card_2]

    return(player_cards,dealer_cards,current_deck)

'''
Player Hits
    -input is current deck, player cards
    -output is new current deck, new player cards
'''
def player_hit (current_deck,player_cards):
    new_card = rand.choice(current_deck)
    player_cards.append(new_card)
    return(current_deck,player_cards)

'''
Dealer Hits
    -input is current deck, dealer cards
    -output is new current deck, new dealer cards
'''
def dealer_hit (current_deck,dealer_cards):
    new_card = rand.choice(current_deck)
    dealer_cards.append(new_card)
    return(current_deck,dealer_cards)

'''
Bust Checker: checks if player or dealer has exceeded 21
    -input: player_cards or dealer_cards
    -output: boolean indicating whether has busted
'''
def bust_checker(input_cards):
    card_total = 0 # initialize variable for card total
    bust = False
    for card in input_cards:
        if len(card) == 2: # check if 2 digit or 3 digit
            try:
                card_total+=int(card[0])
            except: # if face card
                card_total+= 10
        else:
            card_total+=int(card[0]+card[1])
    if card_total > 21:
        bust = True
    else:
        bust = False
    return bust,card_total

"""
Gameplay
"""

'''
First deal
'''
# get a new deck of cards
current_deck = new_deck()

# deal the cards
(player_cards, dealer_cards, current_deck) = deal_cards(current_deck)

# print out the player cards and second computer card
print('Player cards are: ',player_cards)
print('Dealer is showing: ', dealer_cards[1])

'''
User decisions until 'stay'
'''

hit_or_stay = ''

# repeat hit or stay process until the user 'stays'
possibilities = ['h','s']

# ensure user gives valid input
while hit_or_stay not in possibilities or hit_or_stay != 's':

    hit_or_stay = input('Hit or stay? (H/S): ').lower()

    if hit_or_stay == 'h':
        # call player hit fn
        (current_deck,player_cards) = player_hit(current_deck,player_cards)
    elif hit_or_stay == 's':
        pass
    else:
        pass

    print('Player cards are:',player_cards)

    if bust_checker(player_cards)[0] == True:
        print('Player busts, dealer wins!')
        break

'''
Dealer hits until results
'''
print('Dealer cards are', dealer_cards)

while bust_checker(dealer_cards)[1] < 17:
    (current_deck,dealer_cards) = dealer_hit(current_deck,dealer_cards)
    print('Dealer hits! Dealer cards are: ', dealer_cards)

else:
    pass

'''
Game Result
'''

if bust_checker(player_cards)[1] > bust_checker(dealer_cards)[1]:
    print('Player wins with {p} over dealer total of {d}'.format(p = bust_checker(player_cards)[1],
                                                                 d = bust_checker(dealer_cards)[1]))
elif bust_checker(player_cards)[1] < bust_checker(dealer_cards)[1]:
    print('Dealer wins with {d} over player total of {p}'.format(p=bust_checker(player_cards)[1],
                                                                 d=bust_checker(dealer_cards)[1]))
else:
    print('Push! Dealer has {d} and player has {p}'.format(d = bust_checker(dealer_cards)[1],p = bust_checker(player_cards)[1]))
